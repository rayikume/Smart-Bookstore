from  app.Common.Database.models import *
from fastapi import FastAPI , Depends
from sqlalchemy.orm import Session
from db_connection import get_db_connection


class CreateBook:
    def create_book(book :Books,db :Session =Depends(get_db_connection)):
        new_book = Books(**book.dict())
        db.add(new_book)
        db.commit()
        db.refresh(new_book)
        return new_book

class CreateAuthor:
    def create_auther(auther :Authors,db :Session =Depends(get_db_connection)):
        new_author = Authors(**auther.dict())
        db.add(new_author)
        db.commit()
        db.refresh(new_author)
        return new_author
    
class CreateUser:
    def create_user(user :Users,db :Session =Depends(get_db_connection)):
        new_user = Users(**user.dict())
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
    
class CreateUserPreference:
    def create_user_preference(user_preference :UserPreferences,db :Session =Depends(get_db_connection)):
        new_user_preference = UserPreferences(**user_preference.dict())
        db.add(new_user_preference)
        db.commit()
        db.refresh(new_user_preference)
        return new_user_preference