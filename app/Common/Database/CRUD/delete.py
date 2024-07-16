from  app.Common.Database.models import *
from fastapi import FastAPI , Depends, HTTPException ,status, Response
from sqlalchemy.orm import Session
from db_connection import get_db_connection



# will change : 
# (book :Books) -> Books will be the schema for Books, 
class DeleteBook:
    def delete_book(author_id: int, book :Books ,db :Session =Depends(get_db_connection)):
        delete_book = db.query(Books).filter(Books.author_id == author_id)
        if delete_book == None:
            raise HTTPException (status_code=status.HTTP_404_NOT_FOUND, detail=f"Book does not exist")
        else:
            delete_book.delete(synchronize_session=False)
            db.commit()
        return Response(status_code=status.HTTP_204_NO_CONTENT)

# will change : 
# (auther :Authors) -> Authors will be the schema for Authors, 
class DeleteAuthor:
    def delete_auther(author_id : str , auther :Authors,db :Session =Depends(get_db_connection)):
        delete_author = db.query(Authors).filter(Authors.author_id == author_id)
        if delete_author == None:
            raise HTTPException (status_code=status.HTTP_404_NOT_FOUND, detail=f"Author does not exist")
        else:
            delete_author.delete(synchronize_session=False)
            db.commit()
        return Response(status_code=status.HTTP_204_NO_CONTENT)

# will change : 
# (user :Users) , -> Users will be the schema for Users, 
class DeleteUser:
    def delete_user(username : str , user :Users ,db :Session =Depends(get_db_connection)):
        delete_user = db.query(Users).filter(Users.username == username)
        if delete_user == None:
            raise HTTPException (status_code=status.HTTP_404_NOT_FOUND, detail=f"User does not exist")
        else:
            delete_user.delete(synchronize_session=False)
            db.commit()
        return Response(status_code=status.HTTP_204_NO_CONTENT)

# will change : 
# (user_preference :UserPreferences) -> UserPreferences will be the schema for User Preferences, 
# (UserPreferences.preferences == preferences)   -> change the primary key
class DeleteUserPreference:
    def delete_user_preference( username: str , user_preference :UserPreferences,db :Session =Depends(get_db_connection)):
        delete_user_preference = db.query(UserPreferences).filter(UserPreferences.username == username) 
        if delete_user_preference == None:
            raise HTTPException (status_code=status.HTTP_404_NOT_FOUND, detail=f"User preferences does not exist")
        else:
            delete_user_preference.delete(synchronize_session=False)
            db.commit()
        return Response(status_code=status.HTTP_204_NO_CONTENT)