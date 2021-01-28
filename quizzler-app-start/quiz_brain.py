import html

class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        q_text = html.unescape(current_question.text)
        return f"Q.{self.question_number} {q_text}"
        # self.check_answer(user_answer, current_question.answer)

    def still_has_questions(self):
        return self.question_number < len(self.question_list)-1

    def check_answer(self, user_answer):
        correct_answer = self.question_list[self.question_number].answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
        else:
            return False
