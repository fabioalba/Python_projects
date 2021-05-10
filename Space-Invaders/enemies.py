from turtle import Turtle
import random as r


class AliensHorde(Turtle):
    def __init__(self, n_aliens, aliens_padding, move_prob, y_start, pace, ):
        super().__init__()

        self.aliens_padding = aliens_padding
        self.aliens_start_y = y_start

        self.n_aliens = n_aliens
        self.alien_positions = []
        self.aliens_move_prob = move_prob
        self.aliens_pace = pace

        self.aliens_created = []

    def set_positions(self):
       for n in range(self.n_aliens):
            if (n == 0) and (n not in self.alien_positions):
                self.alien_positions.append(n)
            elif n > 0 and ( len(self.alien_positions) < self.n_aliens ):
                self.alien_positions.append(n * self.aliens_padding)

            if n > 0 and ( len(self.alien_positions) < self.n_aliens ):
                self.alien_positions.append(-n * self.aliens_padding)



    def aliens_creation(self):
        for i in self.alien_positions:
            alien = Alien(x=i, y=self.aliens_start_y, move=self.aliens_pace, lives=1, move_prob=self.aliens_move_prob)
            self.aliens_created.append(alien)
        # print(f"Aliens created after alien_creation: {len(self.aliens_created)}")

    def new_level(self):
        self.alien_positions = []
        # print(f"alien positions after level update{self.alien_positions}")

class Alien(Turtle):
    def __init__(self, x, y, move, lives, move_prob ):
        super().__init__()

        # setup
        self.penup()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=1)

        # position and movements
        self.goto(x=x, y=y)
        self.x_move = move
        self.y_move = move
        self.move_prob = move_prob

        self.lives = lives


    def destroyed(self, out_screen_height):
        self.hideturtle()
        self.goto(x=self.xcor(), y=out_screen_height)

    def move_down(self):
        x = r.choice(range(int(self.move_prob)))
        if x == 0:
            new_y = self.ycor() - self.y_move
            self.goto(x=self.xcor(), y=new_y)


