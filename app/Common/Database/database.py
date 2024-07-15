from sqlalchemy import create_engine, Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship, declarative_base, sessionmaker
base = declarative_base()
DATABASE_URL = "postgresql://falsafwan002:Passw0rd@localhost:5432/smart_library"
class Books(base):
    __tablename__= 'books'

    title= Column(String, index=True)
    author_id = Column(Integer, primary_key=True, index=True)
    genre = Column(String, index=True)
    description = Column(String, index=True)
    author = relationship('Authors', back_populates='Books')

class Authors(base):
    __tablename__= 'authors'

    name= Column(String, primary_key=True, index=True)
    biography = Column(String, index=True)
    genre = Column(Integer, primary_key=True, index=True)
    description = Column(Integer, primary_key=True, index=True)
    books = relationship('Books', back_populates='Authors')

class Users(base):
    __tablename__= 'users'

    username= Column(String, primary_key=True, index=True)
    password = Column(String, index=True)
    role = Column(String, index=True)
    description = Column(Integer, primary_key=True, index=True)
    preferences = relationship('UserPreferences', back_populates='Users')


class UserPreferences(base):
    __tablename__= 'userpreferences'

    preferences= Column(String, primary_key=True, index=True)
    author_id = Column(Integer, primary_key=True, index=True)
    genre = Column(Integer, primary_key=True, index=True)
    description = Column(Integer, primary_key=True, index=True)
    user = relationship('Users', back_populates='UserPreferences')
    bookrelation = relationship('Books', back_populates='UserPreferences')


engine = create_engine(DATABASE_URL)

base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


