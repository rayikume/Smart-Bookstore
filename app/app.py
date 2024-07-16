from fastapi import FastAPI # type: ignore
import os
from Common.Database.models import Base
from typing import Annotated, List

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

from fastapi import FastAPI # type: ignore
from Common.Schemas.schemas import Book
import os

books = []

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

@app.get("/books")
async def get_all_books():
    return {"Books": books}

@app.post("/books")
async def add_new_book(book: Book):
    books.append(book)
    return {"Message": "Book Submitted Successfully"}

@app.get("/books/:{book_id}:")
async def search_book_by_id(book_id: int):
    for book in books:
        if book.model_dump()["id"] == book_id:
            return {"Book": book}
    return {"Message": "Book not found"}

@app.put("/books/:{book_id}:")
async def update_book_by_id(book_id: int, updated_book: Book):
    for index, book in enumerate(books):
        if book.model_dump()["id"] == book_id:
            books[index] = updated_book.dict()
            return {"Book": updated_book}
    return {"Message": "Book not found"}

