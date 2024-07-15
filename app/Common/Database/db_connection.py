from fastapi import Depends
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from typing import Annotated
from sqlalchemy.orm import Session


URL_DATABASE= "postgresql://falsafwan002:Passw0rd@localhost:5432/smart_library"

engine= create_engine(URL_DATABASE) 

session_local= sessionmaker(bind= engine , autoflush= False, autocommit = False) 

Base = declarative_base()

def get_db_connection():
    db = session_local()
    try:
        yield db
    finally:
        db.close()

db_dependencies= Annotated[Session, Depends(get_db_connection)]