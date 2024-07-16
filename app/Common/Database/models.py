from sqlalchemy import create_engine, Column, Integer, String, Text, ForeignKey # type: ignore
from sqlalchemy.orm import relationship, declarative_base, sessionmaker # type: ignore
from app.Common.Database.db_connection import Base

class Books(Base):
    __tablename__= 'books'
    book_id = Column(String , primary_key=True, index = True)
    title= Column(String, index=True)
    author_id = Column(Integer, ForeignKey("author_id"), index=True)
    genre = Column(String, index=True)
    description = Column(String, index=True)
    author = relationship('Authors', back_populates='Books')

class Authors(Base):
    __tablename__= 'authors'

    author_name= Column(String, primary_key=True, index=True)
    biography = Column(String, index=True)
    genre = Column(Integer, primary_key=True, index=True)
    description = Column(Integer, primary_key=True, index=True)
    books = relationship('Books', back_populates='Authors')

class Users(Base):
    __tablename__= 'users'

    username= Column(String, primary_key=True, index=True)
    password = Column(String, index=True)
    role = Column(String, index=True)
    description = Column(Integer, primary_key=True, index=True)
    preferences = relationship('UserPreferences', back_populates='Users')


class UserPreferences(Base):
    __tablename__= 'userpreferences'

    preferences= Column(String, primary_key=True, index=True)
    author_id = Column(Integer, primary_key=True, index=True)
    genre = Column(Integer, primary_key=True, index=True)
    description = Column(Integer, primary_key=True, index=True)
    user = relationship('Users', back_populates='UserPreferences')
    bookrelation = relationship('Books', back_populates='UserPreferences')
