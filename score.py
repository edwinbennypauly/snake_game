from turtle import  Turtle
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("highscore.txt",mode="r") as data:
            self.highscore = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        if self.score > self.highscore:
            self.highscore = self.score
            with open("highscore.txt", mode="w") as data:
                data.write(f"{self.highscore}")
        self.update_scoreboard()

    def score_refresh(self):
        self.score = 0
        self.update_scoreboard()

    def high_score_update(self):
        with open("highscore.txt", mode="w") as file:
            file.write(f"{self.highscore}")

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High Score: {self.highscore}", move=False, align="center", font=('Arial', 18, 'normal'))





