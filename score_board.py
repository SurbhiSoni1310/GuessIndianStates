from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.create_board()

    def upgrade(self):
        self.score += 1
        self.clear()
        self.create_board()

    def create_board(self):
        self.hideturtle()
        self.penup()
        self.goto(230, 250)
        self.write(f"Score : {self.score}", align="center", font=("Courier", 24, "normal"))
