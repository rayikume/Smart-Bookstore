from fastapi import Depends
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from typing import Annotated
from sqlalchemy.orm import Session
from sqlalchemy.orm import Session , declarative_base

URL_DATABASE = "postgresql://postgres:aalkathami001:Passw0rd@localhost:5432/smart_library"
# URL_DATABASE = "postgresql://falsafwan002:Passw0rd@localhost:5432/smart_library"
engine = create_engine(URL_DATABASE)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db_connection():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependencies = Annotated[Session, Depends(get_db_connection)]


# Create all tables
Base.metadata.create_all(bind= engine)