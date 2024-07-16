from fastapi import Depends
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.orm import declarative_base  # Use the updated import path
from typing import Annotated

URL_DATABASE = "postgresql://falsafwan002:Passw0rd@localhost:5432/smart_library"

engine = create_engine(URL_DATABASE)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependencies = Annotated[Session, Depends(get_db)]
