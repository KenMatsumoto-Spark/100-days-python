import requests
parameters = {
    "amount": 10,
    "type": "boolean"
}
connection = requests.get("https://opentdb.com/api.php", params=parameters)
data = connection.json()["results"]
question_data = data

# question_data = [
#     {"category": "Entertainment: Comics", "type": "boolean", "difficulty": "hard",
#      "question": "In the comic book &quot;Archie&quot;, Betty is friends with Veronica because she is rich.",
#      "correct_answer": "False", "incorrect_answers": ["True"]},
#     {"category": "Geography", "type": "boolean", "difficulty": "medium",
#      "question": "Israel is 7 hours ahead of New York.", "correct_answer": "True",
#      "incorrect_answers": ["False"]},
#     {"category": "Politics", "type": "boolean", "difficulty": "easy",
#      "question": "Denmark has a monarch.", "correct_answer": "True",
#      "incorrect_answers": ["False"]},
#     {"category": "General Knowledge", "type": "boolean", "difficulty": "easy",
#      "question": "Adolf Hitler was born in Australia. ", "correct_answer": "False",
#      "incorrect_answers": ["True"]},
#     {"category": "Entertainment: Television", "type": "boolean", "difficulty": "easy",
#      "question": "In Battlestar Galactica (2004), Cylons were created by man as cybernetic workers and soldiers.",
#      "correct_answer": "True", "incorrect_answers": ["False"]},
#     {"category": "General Knowledge", "type": "boolean", "difficulty": "medium",
#      "question": "&quot;Santa Claus&quot; is a variety of melon.",
#      "correct_answer": "True", "incorrect_answers": ["False"]},
#     {"category": "Vehicles", "type": "boolean", "difficulty": "easy",
#      "question": "BMW M GmbH is a subsidiary of BMW AG that focuses on car performance.",
#      "correct_answer": "True", "incorrect_answers": ["False"]},
#     {"category": "Science & Nature", "type": "boolean", "difficulty": "medium",
#      "question": "Sound can travel through a vacuum.", "correct_answer": "False",
#      "incorrect_answers": ["True"]},
#     {"category": "Entertainment: Cartoon & Animations", "type": "boolean",
#      "difficulty": "medium",
#      "question": "Blue Danube was one of the musical pieces featured in Disney&#039;s 1940&#039;s film Fantasia.",
#      "correct_answer": "False", "incorrect_answers": ["True"]},
#     {"category": "Entertainment: Television", "type": "boolean", "difficulty": "easy",
#      "question": "&quot;The Simpsons&quot; family is named after creator Matt Groening&#039;s real family.",
#      "correct_answer": "True", "incorrect_answers": ["False"]}
# ]
