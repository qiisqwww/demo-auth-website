from typing import Self
from datetime import date

from pydantic import BaseModel, EmailStr, Field

from src.models import User

__all__ = [
    "UserReturnData"
]


class UserReturnData(BaseModel):
    username: str = Field(min_length=3, max_length=255)
    email: EmailStr = Field(min_length=3, max_length=320)
    birthdate: date
    photo_url: str = Field(min_length=3, max_length=255)
    about: str = Field(max_length=150)
    role: str

    @classmethod
    def from_user(cls, user: User) -> Self:
        return UserReturnData(
            username=user.username,
            email=user.email,
            birthdate=user.birthdate,
            photo_url=user.photo_url,
            about=user.about
        )
