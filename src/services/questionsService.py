from src.openAI_API import OpenAI_API
from src.dbConnection import get_db
from src.models.question import Question
from src.repositories.questionsRepository import QuestionsRepository

question_min_len = 1
question_max_len = 15000


class QuestionsService:

    def __init__(self):
        db = next(get_db())
        self.questionsRepository = QuestionsRepository(db)

    # Validate the body data of request
    def _validate_data(self, data):
        if "question" not in data.keys():
            raise Exception("Invalid request body, question is required")

        question = data["question"]

        if not type(question) == str:
            raise Exception("Question must be of type string")

        if len(question) < question_min_len or len(question) > question_max_len:
            raise Exception("Question length must be between " + str(question_min_len) + " to " + str(question_max_len))

        return question

    def create_question(self, data):
        try:
            question = self._validate_data(data)
        except Exception as e:
            return {"error": str(e)}, 400

        try:
            openAI_API = OpenAI_API()
            answer = openAI_API.ask_openai_api(question)
        except Exception:
            return {"error": "An error has occurred, try again later"}, 500

        # Create Question object
        newQuestion = Question(
            question=question,
            answer=answer
        )

        try:
            # Store the question in the database
            self.questionsRepository.add(newQuestion)
        except Exception:
            return {"error": "An error has occurred, try again later"}, 500

        return {"answer": newQuestion.answer}, 201
