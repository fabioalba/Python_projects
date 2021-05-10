

class CheckVictory():
    def __init__(self, field_size, field, current_player):
        self.game_on = True
        self.field_size = field_size
        self.field = field
        self.current_player = current_player


    def play_again(self):
        a = input("\nDo you want to play again?: ").lower()
        if a == "yes":
            self.game_on = True
            return self.game_on
        elif a == "no":
            print("\nGoodbye!")
            new_game = False
            return new_game

    def draw (self):
        if (self.field.all() != 0) and (self.game_on == True):
           self.game_on = False
           print("No cells available - It's a draw!")
           return self.game_on


    def vertical_win(self, ):
        '''checks for vertical win'''
        for i in range(self.field_size):
            if self.field[0][i] == self.field[1][i] == self.field[2][i] != 0:
                print(f"\nCongratulations Player_{self.current_player}, you win verticaly! | ")
                print(self.field)
                self.game_on = False


    def horizontal_win(self, ):
        '''checks for horizontal win'''

        for row in range(self.field.shape[0]):
            count = (self.field[row] == self.current_player).sum()
            if count == len(self.field[row]):
                print(f"\nCongratulations Player_{self.current_player}, you win horizontally! - ")
                print(self.field)
                self.game_on = False


    def fst_diagonal_win(self, ):
        '''checks for first diagonal win'''
        if self.field[0][0] == self.field[1][1] == self.field[2][2] !=0:
            print(f"\nCongratulations Player_{self.current_player}, you win diagonally! \\ ")
            print(self.field)
            self.game_on = False


    def snd_diagonal_win(self, ):
        '''checks for second diagonal win'''
        index_max = self.field_size - 1
        if self.field[index_max][0] == self.field[index_max-1][1] == self.field[index_max-2][2] != 0:
            print(f"\nCongratulations Player_{self.current_player}, you win diagonally! / ")
            print(self.field)
            self.game_on = False
