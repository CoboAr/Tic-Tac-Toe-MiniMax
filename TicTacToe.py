import math
import time
from Player import AiPlayer,HumanPlayer

# Tic Tac Toe class
class TicTacToe():
    def __init__(self):
        self.board = self.make_board()
        self.current_winner = None
    # create board function
    @staticmethod
    def make_board():
        return [' ' for i in range (9)]
    # print board
    def print_board(self):
        for row in [self.board[i*3:(i+1) * 3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')
    # print board number positions
    @staticmethod
    def print_board_nums():
        # 0 | 1 | 2
        number_board = [[str (i) for i in range (j * 3, (j + 1) * 3)] for j in range (3)]
        for row in number_board:
            print ('| ' + ' | '.join (row) + ' |')
    # make a valid move function
    def make_move(self, position, letter):
        if self.board[position] == ' ':
            self.board[position] = letter
            if self.winner (position, letter):
                self.current_winner = letter
            return True
        return False
    # check if with this move, the player wins the game
    def winner(self, position, letter):
        # check row
        row_index = math.floor(position / 3)
        row = self.board[row_index*3:(row_index+1)*3]
        if all([x == letter for x in row]):
            return True
        # check column
        column_index = position % 3
        column = [self.board[column_index+i*3] for i in range(3)]
        if all([x == letter for x in column]):
            return True
        # check diagonal
        if position % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            # check first diagonal
            if all([x == letter for x in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            # check second diagonal
            if all([x == letter for x in diagonal2]):
                return True
        return False
    # return all empty positions in the board
    def empty_squares(self):
        return ' ' in self.board
    # return the number of empty positions in the board
    def num_empty_squares(self):
        return self.board.count(' ')
    # return a list of all available moves in the board
    def available_moves(self):
        return [i for i, x in enumerate(self.board) if x == " "]
# start game function
def start(tic_tac_toe,start_player,second_player, x_player, o_player, print_game=True):
    if print_game:
        tic_tac_toe.print_board_nums()
    # letter of starting player
    letter = start_player.letter
    # score variables
    global human_score
    global ai_score
    # while there are available positions continue keep playing the game
    while tic_tac_toe.empty_squares ():
        if letter == "X":
            position = x_player.get_move(tic_tac_toe)
        else:
            position = o_player.get_move(tic_tac_toe)

        if tic_tac_toe.make_move(position, letter):
            if print_game:
                print (letter + ' makes a move to position {}'.format (position))
                tic_tac_toe.print_board()
                print ('')
            #if there is a a winner, save the score and return the winning letter
            if tic_tac_toe.current_winner:
                if print_game:
                    if start_player.letter == letter:
                        print (start_player.name + ' wins using '+ letter + " letter!")
                        if start_player.name == "Human player":
                            human_score = human_score + 1
                        else:
                            ai_score = ai_score + 1
                    else:
                        print(second_player.name + " wins using "+ letter + " letter!")
                        if second_player.name == "Human player":
                            human_score = human_score + 1
                        else:
                            ai_score = ai_score + 1
                return letter  # ends the loop and exits the game

            # switches player
            if letter == "X":
                letter = "O"
            else:
                letter= "X"
        # 0.6 seconds for the AI player to make a move
        time.sleep (.6)

    if print_game:
        print ('It\'s a tie!')

if __name__ == '__main__':
    print ('''                 ____ __ ___    ____ __   ___    ____ __ ____     ___   __   _  _ ____ 
                (_  _|  ) __)  (_  _) _\ / __)  (_  _)  (  __)   / __) / _\ ( \/ |  __)
                  )(  )( (__     )(/    ( (__     )((  O ) _)   ( (_ \/    \/ \/ \) _) 
                 (__)(__)___)   (__)_/\_/\___)   (__)\__(____)   \___/\_/\_/\_)(_(____)

                 ''')
    print ("Welcome to Tic Tac Toe game!")

    game_is_on=True
    human_score = 0
    ai_score = 0
    while game_is_on:
        start_game = input ("Do you want to start first? [Yes/No]").lower ()
        while start_game != 'yes' and start_game != 'no':
            start_game = input ("Do you want to start first? [Yes/No]").lower ()

        choice = input ("Please choose if you would like play as X or O: ").lower ()
        while choice != "x" and choice != "o":
            choice = input ("Please choose if you would like play as X or O: ").lower ()

        if start_game == "yes":
            if choice == "x":
                x_player = HumanPlayer ("X")
                o_player = AiPlayer ("O")
                start_player = x_player
                second_player = o_player
            else:
                o_player = HumanPlayer ("O")
                x_player = AiPlayer ("X")
                start_player = o_player
                second_player = x_player
        else:
            if choice == "x":
                o_player = AiPlayer ("O")
                x_player = HumanPlayer ("X")
                start_player = o_player
                second_player = x_player
            else:
                x_player = AiPlayer ("X")
                o_player = HumanPlayer ("O")
                start_player = x_player
                second_player = o_player
        # create an instance of TicTacToe class
        t = TicTacToe ()
        # start the game
        start(t,start_player,second_player,x_player, o_player, print_game=True)
        # print score
        print (f"Score is:\nHuman:{human_score} AI:{ai_score}")
        # ask for a rematch
        rematch = input ("Would you like to play again?[Yes/No]").lower ()
        while rematch != "yes" and rematch != "no":
            rematch = input ("Would you like to play again?[Yes/No]").lower ()
        if rematch == "no":
            game_is_on = False




