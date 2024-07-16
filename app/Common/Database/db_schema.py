from pydantic import BaseModel

class UserSchema(BaseModel):
    user_id : int
    username: str
    email: str
    password: str
    role: str

class BookSchema(BaseModel):
    book_id: str
    title: str
    author_id: int
    genre: str
    description: str

class AuthorSchema(BaseModel):
    author_id= int
    book_id:int
    author_name: str
    biography: str
    genre: str

class UserPreferenceSchema(BaseModel):
    preferences_id: int
    user_id: int
    book_id: int


