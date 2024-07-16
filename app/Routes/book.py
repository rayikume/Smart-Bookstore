from Common.Schemas.base_book import Book
from fastapi import APIRouter

router = APIRouter()

books = []

@router.get("/")
async def get_all_books():
    return {"Books": books}

@router.post("/")
async def add_new_book(book: Book):
    books.append(book)
    return {"Message": "Book Submitted Successfully"}

@router.get("/:{book_id}:")
async def search_book_by_id(book_id: int):
    for book in books:
        if book.model_dump()["id"] == book_id:
            return {"Book": book}
    return {"Message": "Book not found"}

@router.put("/:{book_id}:")
async def update_book_by_id(book_id: int, updated_book: Book):
    for index, book in enumerate(books):
        if book.model_dump()["id"] == book_id:
            books[index] = updated_book
            return {"Message": "Book Updated Successfully"}
    return {"Message": "Book not found"}

@router.delete("/:{book_id}:")
async def delete_book_by_id(book_id: int):
    for index, book in enumerate(books):
        if book.model_dump()["id"] == book_id:
            del books[index]
            return {"Message": "Book Deleted Successfully"}
    return {"Message": "Book not found"}