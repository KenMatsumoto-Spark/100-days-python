from turtle import Screen
import time
from snake import Snake
import food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = food.Food()
score_board = ScoreBoard()

Screen().listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.05)
    snake.move()

#detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score_board.increase_score()

#detect collision with wall.
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        score_board.game_over()

#detect collision with tail.
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 9:
            game_is_on = False
            score_board.game_over()

screen.exitonclick()
