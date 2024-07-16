from fastapi import Depends
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from typing import Annotated
<<<<<<< HEAD
from sqlalchemy.orm import Session
from models import Base 
=======
from sqlalchemy.orm import Session , declarative_base
>>>>>>> 67a375c3d39f51f74b6cbfbc36fd431bf61bbe0e


<<<<<<< HEAD
URL_DATABASE = "postgresql://falsafwan002:Passw0rd@localhost:5432/smart_library"
engine = create_engine(URL_DATABASE)

# Create all tables
Base.metadata.create_all(engine)
=======
engine= create_engine(URL_DATABASE) 
>>>>>>> 67a375c3d39f51f74b6cbfbc36fd431bf61bbe0e

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db_connection():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependencies = Annotated[Session, Depends(get_db_connection)]
