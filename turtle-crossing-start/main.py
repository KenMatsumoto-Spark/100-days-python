import time
from turtle import Screen
from player import Player
import random
from car_manager import CarManager
from scoreboard import Scoreboard

CARS_SPAWN_FACTOR = 4
"""CHANCE OF ONE IN EACH CARS_SPAWN_FACTOR WILL BE GENERATED POR UPDATE"""

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
cars = CarManager()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(player.move, "Up")
current_level = 1

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.move_left()

    #generating random car
    if random.randint(0, CARS_SPAWN_FACTOR) == 0:
        cars.generate_car(current_level)

    #detect level pass
    if player.ycor() > 280:
        cars.erase_all()
        current_level += 1
        scoreboard.update_scoreboard(current_level)
        player.reset_position()

    #detect collision with a car:
    for car in cars.list_cars():
        if player.xcor() > car.xcor()  - 25 and player.xcor() < car.xcor()  + 25 and player.ycor() > car.ycor() - 20 and player.ycor() < car.ycor() + 20:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()