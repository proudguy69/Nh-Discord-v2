from tortoise import Model, fields

class User(Model):
    id = fields.IntField(primary_key=True)
    web_token = fields.CharField(max_length=256)
    access_token = fields.CharField(max_length=256)
    refresh_token = fields.CharField(max_length=256)
    expires = fields.IntField()
    username = fields.CharField(max_length=60)
    user_id = fields.IntField(unique=True)
    avatar = fields.CharField(max_length=256)
