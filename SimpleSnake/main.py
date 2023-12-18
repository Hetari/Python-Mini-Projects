from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


def main():
    # Create a screen
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("My Snake Game")
    screen.tracer(0)

    # Create the objects
    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()

    # Listen for keyboard
    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

    while True:
        screen.update()
        time.sleep(0.1)
        snake.move()

        # Detect collision with food.
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            scoreboard.increase_score()

        # Detect collision with wall.
        if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
            scoreboard.restart()
            snake.reset()
            food.refresh()
            # break

        # Detect collision with tail.
        for segment in snake.segments:
            if segment == snake.head:
                pass
            elif snake.head.distance(segment) < 10:
                scoreboard.restart()
                snake.reset()


if __name__ == '__main__':
    # noinspection PyBroadException
    try:
        main()
    except Exception:
        pass
    except KeyboardInterrupt:
        pass
    finally:
        print('Exit...')
