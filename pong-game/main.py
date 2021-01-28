from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()
screen.tracer(0)


screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #detecting collision with wall
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()

    #detect collision with a paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #detect R paddle miss
    if ball.xcor() > 400:
        scoreboard.l_point()
        ball.reset_position()

    # detect L paddle miss
    if ball.xcor() < -400:
        scoreboard.r_point()
        ball.reset_position()

screen.exitonclick()