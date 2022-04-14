
from typing import List, Optional
from pydantic import BaseModel


class Blog(BaseModel):
    title: str
    body: str

    class Config:
        orm_mode = True


class showUser(BaseModel):
    name: str
    email: str
    blogs: List[Blog] = []

    class Config:
        orm_mode = True


class showBlog(BaseModel):
    title: str
    body: str
    creator: showUser

    class Config:
        orm_mode = True


class User(BaseModel):
    name: str
    email: str
    password: str


class Login(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None
