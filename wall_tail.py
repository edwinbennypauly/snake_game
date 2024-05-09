from turtle import Turtle

class WallTail(Turtle):
    def __init__(self):
        super().__init__()

    def game_over(self):
        self.clear()
        self.color("white")
        self.write("Game Over",align="center",font=('Arial', 18, 'normal'))


