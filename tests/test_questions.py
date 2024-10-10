import pytest
from src.services.questionsService import QuestionsService, question_min_len, question_max_len


@pytest.fixture
def questions_service():
    return QuestionsService()


# Test the method create_question with valid input
def test_create_question_valid_input(questions_service):
    data = {
        "question": "who are you?"
    }

    response, code = questions_service.create_question(data)

    assert code == 201


# Test the method create_question with invalid input type
def test_create_question_invalid_type(questions_service):
    invalid_data = {
        "question": 100
    }

    response, code = questions_service.create_question(invalid_data)

    assert response == {"error": "Question must be of type string"}, 400


# Test the method create_question with invalid input length
def test_create_question_length_too_short(questions_service):
    invalid_data = {
        "question": ""
    }

    response, code = questions_service.create_question(invalid_data)

    assert response == {"error": "Question length must be between " + str(question_min_len) + " to " + str(question_max_len)}, 400