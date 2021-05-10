from turtle import Turtle
from bullet import Bullet


class SpaceShip(Turtle):
    def __init__(self, x, y, move, screen_limit_l, screen_limit_r):
        super().__init__()

        # setup
        self.penup()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)

        # position & movements
        self.goto(x=x, y=y)
        self.x_move = move
        self.y_move = move

        self.right_limit = screen_limit_r
        self.left_limit = screen_limit_l


    def move_left(self):
        if self.xcor() > (self.left_limit * 0.95):
            new_x = self.xcor() - self.x_move
            self.goto(x=new_x, y=self.ycor())


    def move_right(self):
        if self.xcor() < (self.right_limit * 0.95):
            new_x = self.xcor() + self.x_move
            self.goto(x=new_x, y=self.ycor())


    def shoot(self):
        bullet = Bullet(x=self.xcor(), y=self.ycor(), speed=20)
        bullet.move(direction=1)
        return bullet

