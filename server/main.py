from fastapi import FastAPI, Header
from tortoise.contrib.fastapi import register_tortoise
from fastapi.middleware.cors import CORSMiddleware
from aiohttp import ClientSession

# varibles
uri = {
    "dev": "http://localhost:3000",
    "prod": "https://nhdiscord.com"
}.get('dev')

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:3001'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# functions
async def discord_exchange(code):
    pass

# routes

@app.get('/authorize')
async def authorize(code):
    pass