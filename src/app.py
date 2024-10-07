from flask import Flask
from src.models.question import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.routes.questionsRouter import QuestionsRouter

app = Flask(__name__)

# Create a database connection
DATABASE_URL = "postgresql://postgres:12345@localhost:3000/postgres"
engine = create_engine(DATABASE_URL)

# Create a session to the database
Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine)

app.register_blueprint(QuestionsRouter, url_prefix="/ask")

if __name__ == '__main__':
    # Run the Flask server
    app.run(debug=False)
