from fastapi import FastAPI, Header
from tortoise.contrib.fastapi import register_tortoise
from tortoise.exceptions import IntegrityError
from fastapi.middleware.cors import CORSMiddleware
from aiohttp import ClientSession, BasicAuth
from settings import CLIENT_ID, CLIENT_SECRET
from models import User
import time
import secrets

# varibles
uri = {
    "dev": "http://localhost:3001",
    "prod": "https://nhdiscord.com"
}.get('dev')

redirect_uri = {
    "dev": 'http://localhost:3001/authorize'
}.get('dev')

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:3001'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

register_tortoise(
    app,
    db_url="sqlite://database.sqlite3",
    modules={"models":['models']},
    generate_schemas=True
)

# functions
def success(state:bool=True, message:str=None, data:dict=None):
    response = {
        'success': state
    }
    if message: response['message'] = message
    if data:
        for key in data.keys():
            response[key] = data[key]
    return response

async def discord_exchange(code):
    data = {
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': redirect_uri
    }
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    async with ClientSession() as session:
        response = await session.post('https://discord.com/api/v10/oauth2/token', data=data, headers=headers)
        response_data = await response.json()
        return response_data
    
async def user_info(token:str):
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }
    async with ClientSession() as session:
        response = await session.get('https://discord.com/api/v10/users/@me', headers=headers)
        data = await response.json()
        return data
    

# routes

@app.get('/authorize')
async def authorize(code):
    data:dict = await discord_exchange(code)
    if data.get('error'): return success(False, data.get('error_description'))
    ## get user info
    access_token = data.get('access_token')
    if not access_token:
        return success(False, data=data)
    refresh_token = data.get('refresh_token')
    expires_in = data.get('expires_in')
    _user_info:dict = await user_info(access_token)
    d_user_id = _user_info.get('id')
    username = _user_info.get('username')
    avatar_hash = _user_info.get('avatar')
    if not d_user_id: return success(False, data=_user_info)
    # set up varibles
    expires = int(time.time() + expires_in)
    avatar = f'https://cdn.discordapp.com/avatars/{d_user_id}/{avatar_hash}.webp'
    web_token = secrets.token_hex()
    try:
        await User.create(
            web_token=web_token,
            access_token=access_token,
            refresh_token=refresh_token,
            expires=expires,
            username=username,
            user_id=d_user_id,
            avatar=avatar
            )
    except IntegrityError:
        return success(False, 'User already exists')
        
    user = await User.get(web_token=web_token).values('web_token', 'username', 'avatar')
    
    return success(data={'user': user})

@app.get('/logout')
async def logout(authorize:str=Header(None)):
    print(authorize)
    if not authorize: return success(False, 'No token in header')
    user = await User.get_or_none(web_token=authorize)
    print(user)
    if not user: return success(False, 'invalid token in header')
    await user.delete()
    await user.save()
    return success()