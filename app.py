import os
from flask import Flask
from src.dbConnection import SessionLocal
from src.routes.questionsRouter import QuestionsRouter

app = Flask(__name__)

app.register_blueprint(QuestionsRouter, url_prefix="/ask")


# Close the database session after each request
@app.teardown_appcontext
def shutdown_session(exception=None):
    SessionLocal.remove()


if __name__ == '__main__':
    # Run the Flask server
    app.run(debug=False)
