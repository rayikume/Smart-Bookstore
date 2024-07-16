from  app.Common.Database.models import *
from fastapi import FastAPI , Depends
from sqlalchemy.orm import Session
from db_connection import get_db_connection


#GET /books: Retrieve a list of all books.
class ReadBook:
    def read_book(db :Session =Depends(get_db_connection)):
        all_books= db.query(Books).all()
        return all_books
    
#GET /books/:id: Retrieve details of a specific book by its ID.
class ReadSpecificBook:
    def read_specific_book(book_id: int, db :Session =Depends(get_db_connection)):
        specific_book= db.query(Books).filter(Books.book_id == book_id)
        return specific_book
       
class ReadAuthor:
    def read_auther(db :Session =Depends(get_db_connection)):
        all_authers= db.query(Authors).all()
        return all_authers

#GET /authors/:id: Retrieve details of a specific author by their ID.
class ReadSpecificAuthor:
    def read_specific_auther(author_id : int, db :Session =Depends(get_db_connection)):
        specific_auther= db.query(Authors).filter(Authors.author_id == author_id)
        return specific_auther


#POST /users/login: Authenticate a user and return a JWT.
class ReadUser:
    def read_user(db :Session =Depends(get_db_connection)):
        all_users= db.query(Users).all()
        return all_users
    
#GET /users/me: Retrieve the authenticated user's details.
# Authenticatation required
class ReadSpecificUser:
    def read_specific_user(username : str, db :Session =Depends(get_db_connection)):
        specific_user= db.query(Users).filter(Users.username == username)
        return specific_user
    
#GET /recommendations: Retrieve book recommendations for the authenticated user based on their preferences.  
class ReadUserPreference:
    def read_user_preference(username : str, db :Session =Depends(get_db_connection)):
        all_user_preferences= db.query(UserPreferences).filter(Users.username == username)
        return all_user_preferences