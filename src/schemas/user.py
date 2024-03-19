from pydantic import BaseModel
from .note import ShowNote
from typing import List


class UserScheme(BaseModel):
    name: str
    password: str


class ShowUser(BaseModel):
    name: str

    class Config:
        orm_mode = True


class UpdateUser(BaseModel):
    name: str


class CurrentUser(BaseModel):
    user_id: int
    name: str


class ShowMe(BaseModel):
    name: str
    notes: List[ShowNote] = []