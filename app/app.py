from fastapi import FastAPI # type: ignore
import os
from Routes.book import router as book_router
from typing import Annotated, List

app = FastAPI()

app.include_router(book_router, prefix="/books")

@app.get("/")
def read_root():
    return {"Hello": "World"}