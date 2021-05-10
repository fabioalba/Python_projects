import numpy as np
from art import logo
from game_play import GamePlay
from check_victory import CheckVictory



## FIELD AND SETTINGS:
the_field_size = 3
the_field = np.zeros(shape=(the_field_size, the_field_size), dtype=int)


## PLAYERS
Player_1 = 1
Player_2 = 2
players = [Player_1, Player_2]


## CREATE OBJECTS
game = GamePlay()
check_win = CheckVictory(field_size=the_field_size, field=the_field, current_player=game.current_player)


## PLAY THE GAME
print(logo)
print("Welcome to Tic, Tac, Toe!\n")

check_win.game_on = True
while check_win.game_on == True:

    ## choose who is playing at the moment:
    game.define_current_player(player_list=players)
    check_win.current_player = game.current_player

    ## play the players' turn
    game.play_turn(field_size=the_field_size,
                   field=the_field,
                   player_list=players)


    ## check for win:
    check_win.horizontal_win()
    check_win.vertical_win()
    check_win.fst_diagonal_win()
    check_win.snd_diagonal_win()

    check_win.draw()


