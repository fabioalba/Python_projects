from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(x=0, y=0)
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(x=new_x, y=new_y)


    def hit_paddle(self):
        self.y_move *= -1


    def hit_ceiling(self):
        self.y_move *= -1


    def hit_side_wall(self):
        self.x_move *= -1


    def reset_ball(self):
        self.color("black")
        self.goto(x=0, y=0)
        self.color("white")
        self.y_move *= -1


    def hit_top_brick(self):
        ## ball y_move *= -1
        self.y_move *= -1


    def hit_bottom_brick(self):
        ## ball y_move *= -1
        self.y_move *= -1


    def hit_side_brick(self):
        ## ball x_move *= -1
        self.x_move *= -1
