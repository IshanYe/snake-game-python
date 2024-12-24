from food import Food
from snake import Snake
from scoreboard import Scoreboard
import time as ti
import turtle as t

screen = t.Screen()
screen.tracer(0)
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")

snake = Snake(9)
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")

game = True
while game:
    screen.update()
    ti.sleep(0.1)
    snake.move()

    if snake.segments[0].distance(food) < 15:
        food.refresh()
        snake.add_segment()
        scoreboard.increase()

    if (snake.segments[0].xcor() > 280 or snake.segments[0].xcor() < -300 or snake.segments[0].ycor() > 300 or
            snake.segments[0].ycor() < -280):
        game = False
        scoreboard.stop()

    if snake.segments[0].distance(snake.segments[-1].pos()) < 15:
        game = False
        scoreboard.stop()

screen.exitonclick()
