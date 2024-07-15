from fastapi import FastAPI # type: ignore
import os
from app.Common.Database.moels import Base
from typing import Annotated, List

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}



