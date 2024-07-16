from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base  # Import your Base from models.py

URL_DATABASE = "postgresql://falsafwan002:Passw0rd@localhost:5432/smart_library"
engine = create_engine(URL_DATABASE)

# Create all tables
Base.metadata.create_all(engine)

print("Tables created successfully.")