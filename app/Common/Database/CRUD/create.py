from  app.Common.Database.models import *
from fastapi import FastAPI , Depends
from sqlalchemy.orm import Session
from db_connection import get_db_connection
from models import *
from db_schema import*
#POST /books: Create a new book record (Admin only).
class CreateBook:
    def create_book(book :BookSchema,db :Session =Depends(get_db_connection)):
        new_book = Book(**book.dict())
        db.add(new_book)
        db.commit()
        db.refresh(new_book)
        return new_book

#POST /authors: Create a new author record (Admin only).   
class CreateAuthor:
    def create_auther(auther :AuthorSchema,db :Session =Depends(get_db_connection)):
        new_author = Author(**auther.dict())
        db.add(new_author)
        db.commit()
        db.refresh(new_author)
        return new_author

# POST /users/register: Register a new user.
class CreateUser:
    def create_user(user :UserSchema,db :Session =Depends(get_db_connection)):
        new_user = User(**user.dict())
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
    
class CreateUserPreference:
    def create_user_preference(user_preference :UserPreferenceSchema,db :Session =Depends(get_db_connection)):
        new_user_preference = UserPreference(**user_preference.dict())
        db.add(new_user_preference)
        db.commit()
        db.refresh(new_user_preference)
        return new_user_preference