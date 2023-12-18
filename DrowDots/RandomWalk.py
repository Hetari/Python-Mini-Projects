import turtle
import random

turtle.colormode(255)
tim = turtle.Turtle()


def line():
    tim.speed("fastest")
    tim.pensize(15)
    directions = [0, 90, 180, 270]
    for _ in range(500):
        tim.color((random.randint(0, 255), random.randint(
            0, 255), random.randint(0, 255)))

        tim.forward(30)
        tim.setheading(random.choice(directions))


line()

screen = turtle.Screen()
screen.exitonclick()
