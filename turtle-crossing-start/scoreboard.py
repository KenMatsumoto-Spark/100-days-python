from turtle import Turtle

FONT = ("Courier", 12, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super(Scoreboard, self).__init__()
        self.level = 1
        self.penup()
        self.goto(-240, 260)
        self.update_scoreboard(1)
        self.hideturtle()

    def update_scoreboard(self, current_level):
        self.clear()
        self.write(f"Level: {current_level}", align="center", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GameOver!", align="center", font=FONT)