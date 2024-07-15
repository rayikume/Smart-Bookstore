from fastapi import Depends
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from typing import Annotated
from sqlalchemy.orm import Session


URL_DATABASE= "postgresql://falsafwan002:Passw0rd@localhost:5432/smart_library"

engine= create_engine(URL_DATABASE) # Create a new _engine.Engine instance. engine = create_engine("postgresql+psycopg2://scott:tiger@localhost/test")

session_local= sessionmaker(bind= engine , autoflush= False, autocommit = False) # generates new Session objects when called to manage interactions with the database. 
# A session serves as a gateway to the database and provides a way to persist and retrieve Python objects to and from the database.
# sessionmaker(bind=engine) creates a session factory bound to the specified database engine (engine).
# autoflush=False (optional parameter) disables automatic flushing of changes to the database, which can improve performance in some cases.
# used to control whether SQLAlchemy should automatically commit transactions for each individual operation performed within a session

Base = declarative_base()

def get_db_connection():
    db = session_local()
    try:
        yield db
    finally:
        db.close()

db_dependencies= Annotated[Session, Depends(get_db_connection)]