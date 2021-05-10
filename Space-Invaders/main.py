import time
from spaceship import SpaceShip
from turtle import Screen
from bullet import Bullet
from enemies import Alien, AliensHorde
from writings import Writing


DIFFICULTY = 0.5  # rate of increase in enemies' movement, movement probability
FONT = ("Courier", 20, "normal")
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen_limits = {"right_border": (-SCREEN_WIDTH / 2),
                 "left_border": (SCREEN_WIDTH / 2),
                 "bottom_border": (-SCREEN_HEIGHT / 2),
                 "top_border": (SCREEN_HEIGHT / 2)}

ALIENS_DATA = {"number": 5,
               "move_prob": 80,
               "distance": 50,
               "y": 180,
               "pace": 15}

SHIP_DATA = {"x": 0,
             "y": (screen_limits["bottom_border"] * 0.95),
             "pace": 20}

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.tracer()
screen.delay(1)

level = Writing(x=(screen_limits["right_border"] +75),
                y=(screen_limits["top_border"] -50),
                label="Level", font=FONT)

spaceship = SpaceShip(x=SHIP_DATA["x"],
                      y=SHIP_DATA["y"],
                      move=SHIP_DATA["pace"],
                      screen_limit_l=screen_limits["right_border"],
                      screen_limit_r=screen_limits["left_border"])

aliens_horde = AliensHorde(n_aliens=ALIENS_DATA["number"],
                           aliens_padding=ALIENS_DATA["distance"],
                           move_prob=ALIENS_DATA["move_prob"],
                           y_start=ALIENS_DATA["y"],
                           pace=ALIENS_DATA["pace"])

aliens_horde.set_positions()
aliens_horde.aliens_creation()


screen.listen()
screen.onkeypress(fun=spaceship.move_right, key="Right")
screen.onkeypress(fun=spaceship.move_left, key="Left")


bullet_list = []
bullet_speed = 15
play = True
while play == True:
    screen.update()

    ## Check victory
    if aliens_horde.aliens_created == []:
        time.sleep(1)

        ## Next level
        level.update(font=FONT)
        bullet_speed *= (1 + (DIFFICULTY / 2))
        print(f"bullet_speed: {bullet_speed}")

        new_n_aliens = ALIENS_DATA["number"] + (level.level -1)
        new_move_prob = ALIENS_DATA["move_prob"] * (1 - (float(f"0.{level.level}") * (1+DIFFICULTY) ))
        print(f"new_move_prob: {new_move_prob}")

        new_pace = ALIENS_DATA["pace"] * (1 + (float(f"0.{level.level}") * (1+DIFFICULTY) ))
        print(f"new_pace: {new_pace}")

        aliens_horde = AliensHorde(aliens_padding=ALIENS_DATA["distance"],
                                       move_prob=new_move_prob,
                                       n_aliens=new_n_aliens,
                                       pace=new_pace,
                                       y_start=ALIENS_DATA["y"])


        aliens_horde.set_positions()
        aliens_horde.aliens_creation()


    ## Game over
    elif aliens_horde.aliens_created != []:
        for alien in aliens_horde.aliens_created:
            if alien.ycor() <= spaceship.ycor():
                game_over = Writing(x=0, y=0, label="GAME OVER", font=FONT)
                play = False


    ## Aliens move
    for alien in aliens_horde.aliens_created:
        map(alien.move_down(), aliens_horde.aliens_created)

    ## Shoot timing
    if bullet_list == []:
        bullet = Bullet(x=spaceship.xcor(), y=spaceship.ycor(), speed=bullet_speed)
        bullet_list.append(bullet)

    ## Bullet behaviour
    elif bullet_list != []:
        the_bullet = bullet_list[0]
        the_bullet.move(direction=1)

        ## Missed shot
        if the_bullet.ycor() > screen_limits["top_border"]:
            the_bullet.stop(out_screen_height=screen_limits["top_border"] + 10)
            bullet_list.remove(the_bullet)

        ## Detect strike
        for alien in aliens_horde.aliens_created:
            if the_bullet.distance(alien) < 20:
                alien.lives -= 1
                the_bullet.explode(out_screen_height=screen_limits["top_border"]+20)

                ## Kill the alien
                if alien.lives == 0:
                    alien.destroyed(out_screen_height=screen_limits["top_border"] + 20)
                    aliens_horde.aliens_created.remove(alien)


screen.exitonclick()