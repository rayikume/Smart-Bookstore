from  app.Common.Database.models import *
from fastapi import FastAPI , Depends
from sqlalchemy.orm import Session
from db_connection import get_db_connection

class ReadBook:
    def read_book(db :Session =Depends(get_db_connection)):
        all_books= db.query(Books).all()
        return all_books

class ReadAuthor:
    def read_auther(db :Session =Depends(get_db_connection)):
        all_authers= db.query(Authors).all()
        return all_authers
    
class ReadUser:
    def read_user(db :Session =Depends(get_db_connection)):
        all_users= db.query(Users).all()
        return all_users
    
class ReadUserPreference:
    def read_user_preference(db :Session =Depends(get_db_connection)):
        all_user_preferences= db.query(UserPreferences).all()
        return all_user_preferences