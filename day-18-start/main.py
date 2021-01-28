import turtle as t
import random

tim = t.Turtle()
tim.shape("turtle")
tim.color("red")
t.colormode(255)
tim.hideturtle()
tim.speed("fastest")

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

def draw_square_100():
    for _ in range(0, 4):
        tim.forward(100)
        tim.right(90)


def draw_dashed_line():
    for _ in range(0, 15):
        tim.forward(10)
        tim.penup()
        tim.forward(10)
        tim.pendown()


def draw_regular_polygons():
    for sides in range(3, 12):
        for _ in range(0, sides):
            tim.forward(100)
            tim.right(360/sides)


def draw_at_random():
    directions = [0, 90, 180, 270]
    tim.speed(10)
    colors = ["steel blue", "dark cyan", "yellow", "red", "blue", "green", "dark magenta"]
    tim.width(5)
    while True:
        tim.forward(10)
        tim.right(random.choice(directions))
        tim.color(random_color())


def draw_circle(size_f_gap):
    for _ in range(int(360 / size_f_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_f_gap)


def draw_helst():
    tim.penup()
    tim.width(20)
    x, y = (-300, -200)
    tim.setpos(x, y)
    for _ in range(0, 100):
        if _ % 10 == 0 and _ != 0:
            y += 50
            tim.setpos(x, y)
        tim.dot(20, random_color())
        tim.penup()
        tim.forward(50)


draw_helst()
screen = t.Screen()
screen.exitonclick()
