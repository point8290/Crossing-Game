from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.update_score(True)

    def update_score(self, game_on):
        if game_on:
            self.clear()
            self.goto(0, 255)
            self.write(f'Level: {self.level}', align="center", font=("Arial", 30, "normal"))
        else:
            self.clear()
            self.write(f'Game Over Your Level: {self.level}', align="center", font=("Arial", 20, "normal"))


