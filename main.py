import random
import time
from turtle import Screen

from board import Board
from player import Player
from randomCar import RandomCar
from scoreboard import ScoreBoard

CAR_SPEED = 4
screen = Screen()

screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)
screen.listen()

tim = Player()
board = Board(800, 600)
random_cars = []
screen.onkey(tim.up, "Up")
randomCar = RandomCar()
scoreboard = ScoreBoard()
game_on = True
add = False
random_data = list(range(-400, 400))
while game_on:
    add = not add
    time.sleep(CAR_SPEED / 40)
    screen.update()
    if tim.ycor() > 260:
        scoreboard.level += 1
        scoreboard.update_score(game_on)
        CAR_SPEED /= 2
        tim.goto_start()
    position = random.choice(random_data)
    if position % CAR_SPEED == 0:
        randomCar.start(random.choice(board.lanes))
    for car in randomCar.cars:
        car.forward(10)

    for car in randomCar.cars:
        if tim.distance(car) < 20:
            game_on = False

            scoreboard.update_score(game_on)
            break

        if car.xcor() < -400:
            if add:
                y = car.ycor()
                car.goto(400, y)
            else:
                randomCar.cars.remove(car)
                car.goto(1000, 1000)

screen.exitonclick()
