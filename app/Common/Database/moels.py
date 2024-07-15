from sqlalchemy import Boolean , Column , ForeignKey, Integer, String 
from app.Common.Database.db_connection import Base

class Books(Base):
    __tablename__= 'books'

    title= Column(String, index=True)
    author_id = Column(Integer, primary_key=True, index=True)
    genre = Column(String, index=True)
    description = Column(String, index=True)

class Authors(Base):
    __tablename__= 'authors'

    name= Column(String, primary_key=True, index=True)
    biography = Column(String, index=True)
    # genre = Column(Integer, primary_key=True, index=True)
    # description = Column(Integer, primary_key=True, index=True)

class Users(Base):
    __tablename__= 'users'

    username= Column(String, primary_key=True, index=True)
    password = Column(String, index=True)
    role = Column(String, index=True)
    # description = Column(Integer, primary_key=True, index=True)

class UserPreferences(Base):
    __tablename__= 'userpreferences'

    preferences= Column(String, primary_key=True, index=True)
    # author_id = Column(Integer, primary_key=True, index=True)
    # genre = Column(Integer, primary_key=True, index=True)
    # description = Column(Integer, primary_key=True, index=True)