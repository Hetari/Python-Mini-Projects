import turtle
import random


ANGEL = 360
LINE = 10
corner = 3
timmy = turtle.Turtle()
colors = ['red', 'blue', 'green', 'pink', 'purple', 'yellow', 'gray']


def move(angel, corners):
    timmy.color(random.choice(colors))
    for i in range(corners):
        timmy.right(angel / corners)
        timmy.forward(100)
    if corners != 10:
        corners += 1
        move(angel, corners)


move(ANGEL, corner)


screen = turtle.Screen()
screen.exitonclick()
