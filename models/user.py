from datetime import date
from enum import Enum
from typing import Optional

from pydantic import BaseModel


class UserRole(Enum):
    ADMIN = 'ADMIN'
    EDITOR = 'EDITOR'
    MEMBER = 'MEMBER'


class UserSchema(BaseModel):
    name: str
    role: UserRole
    date_joined: date

    class Config:
        schema_extra = {
            "example": {
                "name": "John Doe",
                "role": "MEMBER",
                "date_joined": "2023-01-01",
            }
        }


class UpdateUserModel(BaseModel):
    name: Optional[str]
    role: Optional[UserRole]
    date_joined: Optional[date]

    class Config:
        schema_extra = {
            "example": {
                "name": "John Doe",
                "role": "MEMBER",
                "date_joined": "2023-01-01",
            }
        }
