from fastapi import APIRouter
from Common.Services.book_recommendation import get_recommedation
from Common.Schemas.base_recommendation import Preference

router = APIRouter()

@router.get("/")
def get_book_recommendation(prefrence: Preference):
    genre = prefrence.model_dump()["genre"]
    return get_recommedation(genre)