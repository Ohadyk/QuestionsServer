from flask import Blueprint, request, jsonify
from src.services.questionsService import QuestionsService

QuestionsRouter = Blueprint('question_controller', __name__)
questionsService = QuestionsService()


@QuestionsRouter.route('/', methods=['POST'])
def ask():

    if not request.is_json:
        return jsonify({"error": "Invalid input, JSON required"}), 400

    try:
        data = request.get_json()
    except Exception:
        return jsonify({"error": "Invalid JSON data"}), 400

    response, status_code = questionsService.create_question(data)

    return jsonify(response), status_code
