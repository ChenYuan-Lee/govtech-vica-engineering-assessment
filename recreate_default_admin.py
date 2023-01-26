import asyncio
from datetime import datetime

from fastapi.encoders import jsonable_encoder

from database import delete_user, users_collection
from models.user import UserSchema, UserRole

default_admin_user = UserSchema(
    _id='default_admin',
    name='Default Administrator',
    role=UserRole.ADMIN,
    date_joined=datetime.utcnow().date(),
    password='secret',
)


async def recreate():
    await delete_user(default_admin_user.id)
    await users_collection.insert_one(jsonable_encoder(default_admin_user))

asyncio.run(recreate())
