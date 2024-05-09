from turtle import Screen,Turtle
import time

import food as food
from score import ScoreBoard
from wall_tail import WallTail


import snake




screen = Screen()
screen.bgcolor("black")
screen.setup(width=600,height=600)
screen.title("Classic Snake Game")
screen.tracer(0)
snake = snake.Snake()
food = food.Food()
score_board = ScoreBoard()
wall = WallTail()


screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_on = True

while game_on:
    screen.update()
    time.sleep(0.05)
    snake.snake_movement()


    # detecting collision
    if snake.head.distance(food)<15:
        food.refresh()
        score_board.increase_score()
        snake.snake_growth()

    # collision with wall

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:

        wall.game_over()
        break


    # collision with tail
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) <10:
            game_on = False
            wall.game_over()



















screen.exitonclick()
