THEME_COLOR = "#375362"

from tkinter import *
from quiz_brain import QuizBrain
class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(
            padx=20,
            pady=20,
            bg=THEME_COLOR
        )

        self.score = Label()
        self.score.config(
            text=f"Score: 0",
            bg=THEME_COLOR,
            highlightthickness=0,
            fg="white"
        )
        self.score.grid(column=1, row=0)

        self.canvas = Canvas(
            width=300,
            height=250,
            bg="white"
        )
        self.canvas_text = self.canvas.create_text(
            150,
            125,
            text="Question",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic"),
            width=280
        )

        self.canvas.grid(
            column=0,
            row=1,
            columnspan=2,
            pady=50
        )

        wrong_img = PhotoImage(file="images/false.png")
        right_img = PhotoImage(file="images/true.png")
        self.button_false = Button(
            image=wrong_img,
            highlightthickness=0,
            command=self.false_pressed
        )

        self.button_true = Button(
            image=right_img,
            highlightthickness=0,
            command=self.true_pressed
        )

        self.button_true.grid(
            column=0,
            row=2,
        )

        self.button_false.grid(
            column=1,
            row=2,
        )
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(
            bg="white"
        )
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()

            self.canvas.itemconfig(self.canvas_text, text=q_text)
        else:
            self.canvas.itemconfig(self.canvas_text, text="You reached the end of the quiz!")
            self.button_true.config(state="disabled")
            self.button_false.config(state="disabled")
    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("true"))


    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("false"))


    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(
                bg="green"
            )
        else:
            self.canvas.config(
                bg="red"
            )
        self.window.after(1000, self.get_next_question)
