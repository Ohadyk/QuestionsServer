from src.dbConnection import Session


class QuestionsRepository:

    def __init__(self):
        self.session = Session()

    def add(self, question):
        self.session.add(question)
        self.session.commit()
