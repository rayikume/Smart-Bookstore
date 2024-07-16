from pydantic import BaseModel # type: ignore

class Book(BaseModel):
    id: int
    title: str
    author_id: int
    genre: str
    description: str