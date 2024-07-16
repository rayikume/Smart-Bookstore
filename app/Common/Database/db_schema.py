from pydantic import BaseModel

class UserSchema(BaseModel):
    username: str
    email: str
    password: str
    role: str
    description: str
    preferences: str

class BookSchema(BaseModel):
    book_id: str
    title: str
    author_id: int
    genre: str
    description: str
    author: str

class AuthorSchema(BaseModel):
    author_name: str
    biography: str
    genre: int
    description: str
    books: str

class UserPreferenceSchema(BaseModel):
    preferences: str
    username: str
    author_id: str
    genre: int
    description: str


