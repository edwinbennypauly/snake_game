import random
from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self):
        self.score = None
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.tail = self.segments[len(self.segments)-1]
        self.tail_position = None

    def create_snake(self):
        n,m = 0,0
        for i in range(3):
            snake = Turtle("square")
            snake.color("white")
            snake.penup()
            snake.goto(x=n, y=m)
            snake.speed("fastest")
            self.segments.append(snake)
            n -= 20

    def snake_growth(self):
        snake = Turtle("square")
        snake.color("white")
        snake.penup()
        snake.goto(self.tail_position)
        snake.speed("fastest")
        self.segments.append(snake)





    def snake_movement(self):

        for i in range(len(self.segments) - 1, 0, -1):
            if i == len(self.segments)-1:
                self.tail_position = self.segments[i].position()

            currnent_pos = self.segments[i - 1].position()
            self.segments[i].goto(currnent_pos)
        self.head.forward(MOVE_DISTANCE)


    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)






