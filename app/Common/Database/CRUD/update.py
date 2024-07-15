from  app.Common.Database.models import *
from fastapi import FastAPI , Depends, HTTPException ,status
from sqlalchemy.orm import Session
from db_connection import get_db_connection


# will change : 
# (book :Books) -> Books will be the schema for Books, 
# (Books.author_id == author_id) -> change the primary key to book_id
class UpdateBook:
    def update_book(author_id: int, book :Books ,db :Session =Depends(get_db_connection)):
        update_book = db.query(Books).filter(Books.author_id == author_id)
        update_book.first()
        if update_book == None:
            raise HTTPException (status_code=status.HTTP_404_NOT_FOUND, detail=f"Book does not exist")
        else:
            update_book.update(book.dict(),synchronize_session=False)
            db.commit()
        return update_book.first()

# will change : 
# (auther :Authors) -> Authors will be the schema for Authors, 
# (Authors.name == name) -> change the primary key to auther_id
class UpdateAuthor:
    def update_auther(name : str , auther :Authors,db :Session =Depends(get_db_connection)):
        update_author = db.query(Authors).filter(Authors.name == name)
        update_author.first()
        if update_author == None:
            raise HTTPException (status_code=status.HTTP_404_NOT_FOUND, detail=f"Author does not exist")
        else:
            update_author.update(auther.dict(),synchronize_session=False)
            db.commit()
        return update_author.first()

# will change : 
# (user :Users) , -> Users will be the schema for Users, 
class UpdateUser:
    def update_user(username : str , user :Users ,db :Session =Depends(get_db_connection)):
        update_user = db.query(Users).filter(Users.username == username)
        update_user.first()
        if update_user == None:
            raise HTTPException (status_code=status.HTTP_404_NOT_FOUND, detail=f"User does not exist")
        else:
            update_user.update(user.dict(), synchronize_session=False)
            db.commit()
        return update_user.first()

# will change : 
# (user_preference :UserPreferences) -> UserPreferences will be the schema for User Preferences, 
# (UserPreferences.preferences == preferences)   -> change the primary key
class UpdateUserPreference:
    def update_user_preference( preferences: str , user_preference :UserPreferences,db :Session =Depends(get_db_connection)):
        update_user_preference = db.query(UserPreferences).filter(UserPreferences.preferences == preferences) 
        update_user_preference.first()
        if update_user_preference == None:
            raise HTTPException (status_code=status.HTTP_404_NOT_FOUND, detail=f"User preferences does not exist")
        else:
            update_user_preference.update(user_preference.dict(),synchronize_session=False)
            db.commit()
        return update_user_preference.first()