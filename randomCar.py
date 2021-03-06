import turtle
from turtle import Turtle

turtle.colormode(255)


class RandomCar:
    def __init__(self):
        self.colors = [(185, 162, 114), (119, 186, 136), (140, 70, 123), (130, 103, 61), (133, 157, 194),
                       (191, 135, 173), (77, 92, 140), (149, 154, 62), (210, 243, 219), (180, 89, 151), (246, 223, 240),
                       (204, 215, 121), (77, 167, 96), (70, 123, 86), (134, 226, 158), (205, 219, 242), (108, 101, 189),
                       (56, 41, 147), (117, 31, 112), (228, 164, 210), (175, 172, 236), (185, 102, 88), (70, 154, 168),
                       (26, 47, 81), (72, 24, 67), (234, 172, 161), (87, 89, 18), (137, 214, 226), (67, 47, 20),
                       (27, 90, 57), (23, 62, 39), (115, 44, 32), (198, 218, 19), (18, 83, 97), (68, 36, 232),
                       (28, 246, 144), (135, 26, 231)]
        self.cars = []

    def start(self, y):
        position = (378, y)
        p = Turtle("square")
        p.color(self.colors[y % len(self.colors)])
        p.shapesize(stretch_len=2, stretch_wid=1)
        p.penup()
        p.goto(position)
        p.setheading(180)
        self.cars.append(p)
