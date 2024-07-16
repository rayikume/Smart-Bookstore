from sqlalchemy import Column, Integer, String, Text, ForeignKey 
from sqlalchemy.orm import relationship
from app.Common.Database.db_connection import Base

class Books(Base):
    __tablename__= 'books'
    book_id = Column(Integer , primary_key=True, index = True)
    title= Column(String, index=True)
    author_id = Column(Integer, ForeignKey("author_id"), index=True)
    genre = Column(String, index=True)
    description = Column(Text, index=True)
    author = relationship('Authors', back_populates='Books')

class Book(Base):
    __tablename__ = 'books'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    author_id = Column(Integer, ForeignKey('authors.id'), nullable=False)
    genre = Column(String, nullable=True)
    description = Column(Text, nullable=True)

    author = relationship('Author', back_populates='books')

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True)
    password_hash = Column(String, nullable=False)
    role = Column(String, nullable=False)
    description = Column(Text, nullable=True)

    preferences = relationship('UserPreference', back_populates='user')

class UserPreference(Base):
    __tablename__ = 'user_preferences'
    
    preferences= Column(String,  index=True)
    username = Column(String, ForeignKey("username"), index=True)
    author_id = Column(Integer, ForeignKey("author_id"), index=True)
    genre = Column(Integer, index=True)
    description = Column(Text,  index=True)
    preferences = relationship('Books', back_populates='UserPreferences')


    