# from src.dbConnection import SessionLocal


class QuestionsRepository:

    def __init__(self, db):
        self.db = db

    # Add new question with its answer to the database
    def add(self, question):
        try:
            self.db.add(question)
            self.db.commit()
        except Exception:
            raise Exception("Database error")
