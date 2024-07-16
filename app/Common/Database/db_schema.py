from pydantic import BaseModel
from app.Common.Database.models import *
class user(BaseModel):
    username: str
    email: str
    password: str
    role : str
    description:str
    preferences: str


class book(BaseModel):
    book_id: str
    title: str
    author_id: int
    genre: str
    description: str
    author: str


class author(BaseModel):
    author_name: str
    biography: str
    genre: int
    description: str
    books: str



class userPreference(BaseModel):
    preferences: str
    username: str
    author_id: str
    genre: int
    description: str
