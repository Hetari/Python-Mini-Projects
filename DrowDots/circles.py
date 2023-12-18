import turtle
import random


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


turtle.colormode(255)
tom = turtle.Turtle()

current_heading = -1
while not current_heading == 355:
    tom.speed('fastest')
    tom.color(random_color())
    tom.circle(100)
    current_heading = tom.heading()
    tom.setheading(current_heading + 5)


screen = turtle.Screen()
screen.exitonclick()
