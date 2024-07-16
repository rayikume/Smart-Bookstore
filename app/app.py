from fastapi import FastAPI # type: ignore
import os
from Routes.book import router as book_router
from typing import Annotated, List
from Common.Database.db_connection import *
app = FastAPI()

app.include_router(book_router, prefix="/books")
Base.metadata.create_all(bind= engine)

@app.get("/")
def read_root():
    return {"Hello": "World"}