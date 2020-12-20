from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("red")
        self.penup()
        self.goto_start()
        self.setheading(90)

    def goto_start(self):
        self.goto(0, -280)

    def up(self):
        self.forward(10)
