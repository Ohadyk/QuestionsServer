from flask import Flask
from src.routes.questionsRouter import QuestionsRouter

app = Flask(__name__)

app.register_blueprint(QuestionsRouter, url_prefix="/ask")

if __name__ == '__main__':
    # Run the Flask server
    app.run(debug=False)
