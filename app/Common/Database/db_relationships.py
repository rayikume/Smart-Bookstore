from models import * 
from sqlalchemy.orm import relationship
books = relationship('Book', back_populates='authors')
author = relationship('Author', back_populates='books')
preferences = relationship('UserPreference', back_populates='users')
user = relationship('User', back_populates='user_preferences')
books = relationship('Book', back_populates='user_preferences')
