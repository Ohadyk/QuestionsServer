from flask import Blueprint, request, jsonify
from src.services.questionsService import QuestionsService

QuestionsRouter = Blueprint('question_controller', __name__)
questionsService = QuestionsService()


@QuestionsRouter.route('/', methods=['POST'])
def ask():
    data = request.get_json()

    response, status_code = questionsService.create_question(data)

    return jsonify(response), status_code
