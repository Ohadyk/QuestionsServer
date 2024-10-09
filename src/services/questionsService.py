import os
from openai import OpenAI
from src.dbConnection import get_db
from src.models.question import Question
from src.repositories.questionsRepository import QuestionsRepository

question_min_len = 1
question_max_len = 1000


class QuestionsService:

    def __init__(self):
        db = next(get_db())
        self.questionsRepository = QuestionsRepository(db)

    # Validate the body data of request
    def validate_data(self, data):
        if "question" not in data.keys():
            raise Exception("Invalid request body, question is required")

        question = data["question"]

        if not type(question) == str:
            raise Exception("Question must be of type string")

        if len(question) < question_min_len or len(question) > question_max_len:
            raise Exception("Question length must be between " + str(question_min_len) + " to " + str(question_max_len))

        return question

    # Send question to OpenAI API to get the answer
    def ask_openai_api(self, question):
        client = OpenAI(
            api_key=os.getenv('OPENAI_API_KEY'),
            organization=os.getenv('OPENAI_ORGANIZATION'),
            project=os.getenv('OPENAI_PROJECT'),
        )

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": question}
            ],
        )

        # Extract the answer from the API response
        answer = response.choices[0].message.content.strip()

        return answer

    def create_question(self, data):
        try:
            question = self.validate_data(data)
        except Exception as e:
            return {"message": str(e)}, 400

        try:
            answer = self.ask_openai_api(question)
        except Exception:
            return {"message": "An error has occurred, try again later"}, 500

        # Create Question object
        newQuestion = Question(
            question=question,
            answer=answer
        )

        try:
            # Store the question in the database
            self.questionsRepository.add(newQuestion)
        except Exception:
            return {"message": "An error has occurred, try again later"}, 500

        return {"answer": newQuestion.answer}, 201
