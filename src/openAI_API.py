import os
from openai import OpenAI


class OpenAI_API:

    def __init__(self):
        self.client = OpenAI(
            api_key=os.getenv('OPENAI_API_KEY'),
            organization=os.getenv('OPENAI_ORGANIZATION'),
            project=os.getenv('OPENAI_PROJECT'),
        )

    def ask_openai_api(self, question):

        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": question}
            ],
        )

        # Extract the answer from the API response
        answer = response.choices[0].message.content.strip()

        return answer
