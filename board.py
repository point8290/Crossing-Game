from turtle import Turtle


class Board(Turtle):
    def __init__(self, width, height):
        super().__init__("turtle")
        self.color("white")
        self.hideturtle()
        self.penup()

        i = 240
        self.lanes = []
        while i > -240:
            self.lanes.append((i - 20))
            position = (380, i)
            i -= 60


