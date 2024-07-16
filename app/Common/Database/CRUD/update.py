from  app.Common.Database.models import *
from fastapi import FastAPI , Depends, HTTPException ,status
from sqlalchemy.orm import Session
from app.Common.Database.db_connection import get_db_connection
from app.Common.Database.db_schema import *


# will change : 
# (book :Books) -> Books will be the schema for Books, 
# PUT /books/:id: Update an existing book record by its ID (Admin only).
class UpdateBook:
    def update_book(book_id: int, book :Books ,db :Session =Depends(get_db_connection)):
        update_book = db.query(Books).filter(Books.book_id == book_id)
        update_book.first()
        if update_book == None:
            raise HTTPException (status_code=status.HTTP_404_NOT_FOUND, detail=f"Book does not exist")
        else:
            update_book.update(book.dict(),synchronize_session=False)
            db.commit()
        return update_book.first()
    print ("hi ")

# will change : 
# (auther :Authors) -> Authors will be the schema for Authors, 
#PUT /authors/:id: Update an existing author record by their ID (Admin only).
class UpdateAuthor:
    def update_auther(author_id : str , auther :Authors,db :Session =Depends(get_db_connection)):
        update_author = db.query(Authors).filter(Authors.author_id == author_id)
        update_author.first()
        if update_author == None:
            raise HTTPException (status_code=status.HTTP_404_NOT_FOUND, detail=f"Author does not exist")
        else:
            update_author.update(auther.dict(),synchronize_session=False)
            db.commit()
        return update_author.first()

# will change : 
# (user :Users) , -> Users will be the schema for Users, 
#PUT /users/me: Update the authenticated user's information.
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
class UpdateUserPreference:
    def update_user_preference( username: str , user_preference :UserPreferences,db :Session =Depends(get_db_connection)):
        update_user_preference = db.query(UserPreferences).filter(UserPreferences.username == username) 
        update_user_preference.first()
        if update_user_preference == None:
            raise HTTPException (status_code=status.HTTP_404_NOT_FOUND, detail=f"User preferences does not exist")
        else:
            update_user_preference.update(user_preference.dict(),synchronize_session=False)
            db.commit()
        return update_user_preference.first()