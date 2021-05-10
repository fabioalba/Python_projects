from turtle import Turtle
import random as r

class Brick(Turtle):
    def __init__(self, width, height, x, y):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=height, stretch_len=width)
        self.color("white")
        self.penup()
        self.speed(0.1)
        self.goto(x=x, y=y)

    def disappear(self):
        # self.color("black")
        self.speed(0.1)
        self.goto(x=2000, y=2000)



