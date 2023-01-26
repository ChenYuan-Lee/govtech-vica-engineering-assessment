from fastapi import APIRouter, HTTPException
from fastapi.encoders import jsonable_encoder

from database import add_user, delete_user, update_user
from models.user import UserSchema, UpdateUserModel

router = APIRouter(prefix="/user", tags=["user"])


@router.post("/", response_description="User added into the database")
async def add_user_data(user: UserSchema):
    user = jsonable_encoder(user)
    new_user = await add_user(user)
    return new_user


@router.put("/{id}")
async def update_user_data(id: str, req: UpdateUserModel):
    req = {k: v for k, v in req.dict().items() if v is not None}
    req = jsonable_encoder(req)
    user_updated = await update_user(id, req)
    if user_updated:
        return f"User {id} updated"
    else:
        raise HTTPException(status_code=404, detail=f"There was an error updating user {id}")


@router.delete("/{id}", response_description="User data deleted from the database")
async def delete_user_data(id: str):
    user_deleted = await delete_user(id)
    if user_deleted:
        return f"User {id} deleted successfully"
    else:
        raise HTTPException(status_code=404, detail=f"User {id} does not exist")
