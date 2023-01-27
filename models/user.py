from datetime import date
from enum import Enum
from typing import Optional

from passlib.context import CryptContext
from pydantic import BaseModel, validator, Field

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class UserRole(Enum):
    ADMIN = 'ADMIN'
    EDITOR = 'EDITOR'
    MEMBER = 'MEMBER'


class UserSchema(BaseModel):
    id: str = Field(alias='_id')
    name: str
    role: UserRole
    date_joined: date
    password: Optional[str]

    @validator('password', always=True)
    def hash_password(cls, password: Optional[str], values):
        user_role = values['role']
        if (user_role is UserRole.ADMIN or user_role is UserRole.EDITOR) and password is None:
            raise ValueError('password must be set for ADMIN/EDITOR user')

        return pwd_context.hash(password)

    class Config:
        schema_extra = {
            "example": {
                "_id": "john_doe",
                "name": "John Doe",
                "role": "MEMBER",
                "date_joined": "2023-01-01",
                "password": "secret",
            }
        }


class UpdateUserModel(BaseModel):
    name: Optional[str]
    role: Optional[UserRole]
    date_joined: Optional[date]

    class Config:
        schema_extra = UserSchema.Config.schema_extra
