from flask import Blueprint
from src.controllers.questionsController import QuestionsController

QuestionsRouter = Blueprint('question_controller', __name__)

QuestionsRouter.route('/',methods=['POST'])(QuestionsController.ask)