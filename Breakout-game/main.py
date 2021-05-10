from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from bricks import Brick

from writing import Writing
import random as r
import time



# create screen
screen = Screen()
screen_height = 600
screen_width = 800
screen.bgcolor("black")
screen.setup(width=screen_width, height=screen_height)
screen.title("Breakout")
screen.tracer()


# create objects
paddle = Paddle(screen_w=screen_width, screen_h=screen_height, move=40)
ball = Ball()


# create labels
label_position_x = (screen_width / 2) - (screen_width * 0.10)
label_position_y = (screen_height / 2) - (screen_height * 0.10)

lives_board = Writing(x=(label_position_x * -1), y=label_position_y, label="Lives")
score_board = Writing(x=label_position_x, y=label_position_y, label="Score")
level_board = Writing(x=0, y=label_position_y, label="Level")


# paddle commands
screen.listen()
screen.onkeypress(paddle.move_right, "Right")
screen.onkeypress(paddle.move_left, "Left")


# _______________________ ROW OF BRICKS ______________________#

row_y = 200  #brick line y coor
row_height = 1 #brick row height, not in pixels

screen_limits_x = [-screen_width/2, screen_width/2]
brick_list = []

padding = 2 #space between bricks, bricks and walls

brick_w = 3
brick_w_pixels = brick_w * 20

beg_brick = screen_limits_x[0] + padding
end_brick = beg_brick + brick_w_pixels
x_first_brick = beg_brick + (brick_w_pixels / 2)
first_brick = Brick(width=brick_w, height=row_height, x=x_first_brick, y=row_y)
brick_list.append(first_brick)

while end_brick <= (screen_limits_x[1] - 50):
    brick_w = r.randint(2, 4)
    brick_w_pixels = brick_w * 20
    beg_brick = end_brick + padding
    end_brick = beg_brick + brick_w_pixels

    x_new_brick = beg_brick + (brick_w_pixels / 2)

    new_brick = Brick(width=brick_w, height=row_height, x=x_new_brick, y=row_y)

    brick_list.append(new_brick)



#__________________________GAME DYNAMICS___________________________#

wall_x = (screen_width / 2) - 20
play = True
while play == True:
    screen.update()
    ball.move()


    ## detect collision with walls
    if ball.xcor() < (- wall_x) or ball.xcor() > wall_x:
        ball.hit_side_wall()


    ## detect collision with paddle
    if ball.distance(paddle) < 90 and ball.ycor() < - 270:
        ball.hit_paddle()


    ## detect collision with ceiling
    ceiling_y = screen_height / 2 - 20
    if ball.ycor() > ceiling_y:
        ball.hit_ceiling()


    ## detect collision with floor:
    if ball.ycor() <= -300:
        ball.reset_ball()
        paddle.reset_position()
        lives_board.update()
        time.sleep(2)

        ## check game_over
        if lives_board.lives == 0:
            score_board.score = 0
            play = False
            lose = Writing(x=0, y=0, label="Game over.")
            time.sleep(3)

    ## detect collision with brick
    for brick in brick_list:
        if ball.distance(brick) < 50:
            ball.hit_bottom_brick()
            brick.disappear()
            score_board.update()
            brick_list.remove(brick)
            if brick_list == []:
                win = Writing(x=0, y=0, label="YOU WIN!")
                play = False
                # ball.reset_ball()

screen.exitonclick()

