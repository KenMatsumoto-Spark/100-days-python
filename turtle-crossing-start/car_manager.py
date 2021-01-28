from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
cars = []

class CarManager():
    def __init__(self):
        self.cars = []

    def generate_car(self, current_level):
        new_car = Turtle()
        new_car.level = current_level
        new_car.penup()
        new_car.shape("square")
        new_car.shapesize(stretch_len=1.5)
        new_car.setheading(180)
        new_car.color(random.choice(COLORS))
        random_y_position = random.randint(-250, 250)
        new_car.goto(300, random_y_position)
        self.cars.append(new_car)

    def move_left(self):
        for car in self.cars:
            car.forward(STARTING_MOVE_DISTANCE + (car.level-1)*MOVE_INCREMENT)

    def erase_all(self):
        for car in self.cars:
            car.goto(-400, 0)

    def list_cars(self):
        return self.cars