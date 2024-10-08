from src.models.question import Question
from src.repositories.questionsRepository import QuestionsRepository

question_min_len = 1
question_max_len = 10


class QuestionsService:

    def __init__(self):
        self.questionsRepository = QuestionsRepository()

    # Validate the body data of the request
    def validate_data(self, data):
        if "question" not in data.keys():
            raise Exception("Invalid request body, question is required")

        question = data["question"]

        if not type(question) == str:
            raise Exception("Question must be of type string")

        if len(question) < question_min_len or len(question) > question_max_len:
            raise Exception("Question length must be between " + str(question_min_len) + " to " + str(question_max_len))

    def create_question(self, data):
        try:
            self.validate_data(data)
        except Exception as e:
            return {"message": str(e)}, 400

        # Create Question object
        newQuestion = Question(
            question=data["question"],
            answer="answer"
        )

        # Store the question in the database
        self.questionsRepository.add(newQuestion)

        return {"message": newQuestion.answer}, 201
