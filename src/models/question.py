from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String

# Define the base class for declarative models
Base = declarative_base()


# Define the Question entity
class Question(Base):

    # Table name in the database
    __tablename__ = 'questions'

    # Define the columns for the table
    id = Column(Integer, primary_key=True, autoincrement=True)
    question = Column(String, nullable=False)
    answer = Column(String, nullable=False)
