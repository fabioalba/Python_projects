from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, screen_w, screen_h, move):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=10)
        self.penup()
        self.speed(0.1)
        self.move = move

        initial_y = (-screen_h/2)*0.95
        self.goto(x=0, y=initial_y)

        self.right_limit = screen_w/2
        self.left_limit = - screen_w/2


    def move_right(self):
        if self.xcor() < (self.right_limit * 0.95):
            new_x = self.xcor() + self.move
            self.goto(x=new_x, y=self.ycor())

    def move_left(self):
        if self.xcor() > (self.left_limit * 0.95):
            new_x = self.xcor() - 30
            self.goto(x=new_x, y=self.ycor())

    def reset_position(self):
        self.goto(x=0, y=self.ycor())


