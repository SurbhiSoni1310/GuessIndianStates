from turtle import Turtle


class Label(Turtle):
    def __init__(self, position, name):
        super().__init__()
        self.create_label(position, name)

    def create_label(self, position, name):
        self.hideturtle()
        self.penup()
        self.goto(position)
        self.write(name, align="center", font=("Ariel", 13, "normal"))

