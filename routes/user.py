from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder

from database import add_user, delete_user
from models.user import UserSchema

router = APIRouter(prefix="/user", tags=["user"])


@router.post("/", response_description="User added into the database")
async def add_user_data(user: UserSchema):
    user = jsonable_encoder(user)
    new_user = await add_user(user)
    return new_user


@router.delete("/{id}", response_description="User data deleted from the database")
async def delete_user_data(id: str):
    user_deleted = await delete_user(id)
    if user_deleted:
        return f"User {id} deleted successfully"

    return f"User {id} does not exist"
