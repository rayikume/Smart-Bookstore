from Routes.book import get_all_books

db_book = get_all_books()["Books"]

recommended_books = []

def get_recommedation(genre):
    for book in db_book:
        if genre == book.model_dump()["genre"]:
            recommended_books.append(book)
    return {"Recommended_Books:": recommended_books}
    


