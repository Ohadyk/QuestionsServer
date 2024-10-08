from src.models.question import Question
from src.repositories.questionsRepository import QuestionsRepository


class QuestionsService:

    def __init__(self):
        self.questionsRepository = QuestionsRepository()

    def create_question(self, data):

        # Create Question object
        newQuestion = Question(
            question=data["question"],
            answer="answer"
        )

        # Store the question in the database
        self.questionsRepository.add(newQuestion)

        return {"message": newQuestion.answer}, 201