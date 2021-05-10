from turtle import Turtle


class Bullet(Turtle):
    def __init__(self, x, y, speed):
        super().__init__()

        # setup
        self.hideturtle()
        self.penup()
        self.color("white")

        self.shape("square")
        self.shapesize(stretch_wid=0.5, stretch_len=0.2)

        self.goto(x=x, y=y)
        self.y_move = speed
        self.speed(0.4)


    def move(self, direction):
        self.showturtle()
        new_y = self.ycor() + (self.y_move * direction)
        new_x = self.xcor()
        self.goto(x=new_x, y=new_y)

    def stop(self, out_screen_height):
        self.goto(x=self.xcor(), y=out_screen_height)


    def explode(self, out_screen_height):
        self.hideturtle()
        self.goto(x=self.xcor(), y=out_screen_height)




