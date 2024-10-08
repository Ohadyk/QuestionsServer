from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.models.question import Base

# Create a database connection
DATABASE_URL = "postgresql://postgres:12345@localhost:3000/postgres"
engine = create_engine(DATABASE_URL)

# Create a session to the database
Session = sessionmaker(bind=engine)

Base.metadata.create_all(engine)
