from pydantic import BaseModel
from typing import Optional, Union


class Blog(BaseModel):
     title: str
     body: str
     published: Optional[bool] = None


class User(BaseModel):
    name: str
    email: str
    password: str


class ShowUser(BaseModel):
    name: str
    email: str
    blogs: list[Blog] = []



class ShowBlog(BaseModel):
    title: str
    body: str
    creator: ShowUser


class Login(BaseModel):
    username: str
    password: str



class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Union[str, None] = None


