from turtle import Turtle
FONT = ("", 20, "")


class Writing(Turtle):
    def __init__(self, label, x, y):
        super().__init__()
        self.hideturtle()
        self.goto(x=x, y=y)
        self.color("white")

        self.lives = 3
        self.score = 0
        self.level = 1
        self.label = label.lower()

        if self.label == "score":
            self.write(arg=f"{label}: {self.score}", font=FONT, align="center")
        elif self.label == "lives":
            self.write(arg=f"{label}: {self.lives}", font=FONT, align="center")
        elif self.label == "level":
            self.write(arg=f"{label}: {self.level}", font=FONT, align="center")

        # win or lose
        elif self.label == "you win!":
            self.write(arg=f"{label}", font=FONT, align="center")
        elif self.label == "game over.":
            self.write(arg=f"{label}", font=FONT, align="center")


    def update(self):
        self.clear()
        if self.label.lower() == "lives":
            self.lives -= 1
            self.write(arg=f"{self.label}:{self.lives}", font=FONT, align="center")
        elif self.label.lower() == "score":
            self.score += 10
            self.write(arg=f"{self.label}:{self.score}", font=FONT, align="center")
        elif self.label.lower() == "level":
            self.level += 1
            self.write(arg=f"{self.label}:{self.level}", font=FONT, align="center")


