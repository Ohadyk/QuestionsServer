import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from src.models.question import Base
from dotenv import load_dotenv

load_dotenv()

# Create a database connection
DATABASE_URL = os.getenv('DATABASE_URL')
engine = create_engine(DATABASE_URL)

# Create a session to the database
Session_factory = sessionmaker(bind=engine)
SessionLocal = scoped_session(Session_factory)

# Initialize the database
Base.metadata.create_all(engine)


# Return session to the database
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
