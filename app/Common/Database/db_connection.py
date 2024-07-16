from fastapi import Depends
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from typing import Annotated
from sqlalchemy.orm import Session
from sqlalchemy.orm import Session , declarative_base
from sqlalchemy_utils import database_exists, create_database
from app.Common.Database.models import Base

#URL_DATABASE = "postgresql://postgres:aalkathami001:Passw0rd@localhost:5432/postgres"
URL_DATABASE = "postgresql://falsafwan002:Passw0rd@localhost:5432/smart_library"
engine = create_engine(URL_DATABASE)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Check if the database exists, create if it doesn't
if not database_exists(engine.url):
    create_database(engine.url)
# Drop all tables
Base.metadata.drop_all(engine)
# Create all tables
Base.metadata.create_all(bind= engine)
Base = declarative_base()

def get_db_connection():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependencies = Annotated[Session, Depends(get_db_connection)]


