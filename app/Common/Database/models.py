from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Author(Base):
    __tablename__ = 'authors'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    biography = Column(Text, nullable=True)

    books = relationship('Book', back_populates='authors')

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
    preferences = relationship('UserPreference', back_populates='users')

class UserPreference(Base):
    __tablename__ = 'user_preferences'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    book_id = Column(Integer, ForeignKey('books.id'), nullable=False)
    preference = Column(Text, nullable=True)  
    user = relationship('User', back_populates='user_preferences')
    books = relationship('Book', back_populates='user_preferences')