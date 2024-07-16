from fastapi import FastAPI # type: ignore
import os
from Routes.book import router as book_router
from typing import Annotated, List

app = FastAPI()

<<<<<<< HEAD
@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

from fastapi import FastAPI # type: ignore
from Common.Schemas.schemas import Book
import os
from typing import Annotated, List
from Common.Database.db_connection import *

books = []

app = FastAPI()
Base.metadata.create_all(bind=engine)
=======
app.include_router(book_router, prefix="/books")

@app.get("/")
>>>>>>> origin
def read_root():
    return {"Hello": "World"}