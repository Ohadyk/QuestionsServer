from flask import request, jsonify


class QuestionsController:

    def ask():
        # Get data from the request body
        data = request.get_json()

        # Process the data (for now, just echo it back)
        response = {
            'received_data': data
        }

        return jsonify(response), 200
