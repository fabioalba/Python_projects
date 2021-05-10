from turtle import Turtle


class Writing(Turtle):
    def __init__(self, x, y, label, font):
        super().__init__()

        # setup
        self.penup()
        self.color("white")
        self.hideturtle()
        self.label = label.lower()
        self.level = 1

        # position
        self.goto(x=x, y=y)
        self.speed(0.1)

        if self.label == "level":
            self.write(arg=f"{label}:{self.level}", font=font, align="center")
        else:
            self.write(arg=label, font=font, align="center")


    def update(self, font):
        self.clear()
        if self.label == "level":
            self.level += 1
            self.write(arg=f"{self.label.capitalize()}:{self.level}", font=font, align="center")


