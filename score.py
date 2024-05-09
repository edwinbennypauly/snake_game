from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0,270)

        self.hideturtle()

    def increase_score(self):
        self.clear()
        self.score += 1
        self.write(arg=f"Score : {self.score}", move=False, align="center",font=('Arial', 18, 'normal'))

