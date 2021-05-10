

class GamePlay():
    def __init__(self):
        self.turn = 0
        self.current_player = ""

    def define_current_player(self, player_list):
        '''Returns which player is currently playing'''

        if self.turn < 2:
            self.current_player = player_list[self.turn]

            # print(f"This is Player_{self.current_player}'s turn.")
            # return self.current_player

        elif self.turn >= 2:
            index = self.turn % len(player_list)
            self.current_player = player_list[index]

        print(f"This is Player_{self.current_player}'s turn.")
        return self.current_player


    def play_turn(self, field_size, field, player_list):
        '''Allows play to insert its mark and checks if call is correct'''

        global turn
        correct_move = False
        while correct_move == False:

            choose_row = (input(f"Player {self.current_player}, which row to play?: "))
            choose_column = (input("Which column?: "))

            # enter a letter
            try:
                choose_row = int(choose_row)
                try:
                    choose_column = int(choose_column)


                    # position not in field size:
                    if choose_row >= field_size:
                        print(f"Row is too big. Please choose between 0 and {field_size-1}\n")
                    elif choose_column >= field_size:
                        print(f"Column is too big. Please choose between 0 and {field_size-1}\n")

                    # position already occupied:
                    elif field[choose_row][choose_column] in player_list:
                        print("You've chosen an occupied place. Please choose another.\n")


                    # right call:
                    elif field[choose_row][choose_column] == 0:
                        field[choose_row][choose_column] = self.current_player
                        self.turn += 1
                        correct_move = True
                        print(f"\nTurn {self.turn} - Current board: \n{field}\n")

                except ValueError:
                    if (isinstance(choose_column, int) == False):
                        print(f"Please enter a number from {range(field_size)[0]} to {range(field_size)[-1]}\n")

            except ValueError:
                if (isinstance(choose_row, int) == False):
                    print(f"Please enter a number from {range(field_size)[0]} to {range(field_size)[-1]}\n")


