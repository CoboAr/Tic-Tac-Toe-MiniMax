import math
import random
# Player class
class Player():
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        pass
# Human player class
class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
        self.name = "Human player"
    # check if the move of Human player is valid
    def get_move(self, game):
        valid_position = False
        value = None
        while not valid_position:
            position = input (self.letter + '\'s turn. Input move (0-8): ')
            try:
                value = int (position)
                if value not in game.available_moves ():
                    raise ValueError
                valid_position = True
            except ValueError:
                print ('Invalid square. Try again.')
        return value
# AI Player class
class AiPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
        self.name = "Ai Player"
    # If AI player starts first, choose a random position to start the game.
    def get_move(self, tic_tac_toe):
        if len(tic_tac_toe.available_moves()) == 9:
            position = random.choice(tic_tac_toe.available_moves())
        else:
            position = self.minimax(tic_tac_toe, self.letter)['position']
        return position

    # Use the minimax algorithm to determine the best move
    def minimax(self, state, player):
        max_player = self.letter  # yourself
        other_player = 'O' if player == 'X' else 'X'

        # Check if the previous move is a winner
        if state.current_winner == other_player:
            return {'position': None,
                    'score': 1 * (state.num_empty_squares () + 1) if other_player == max_player else -1 * (
                            state.num_empty_squares () + 1)}
        elif not state.empty_squares ():
            return {'position': None, 'score': 0}

        if player == max_player:
            best = {'position': None, 'score': -math.inf}  # each score should maximize
        else:
            best = {'position': None, 'score': math.inf}  # each score should minimize
        for possible_move in state.available_moves ():
            state.make_move (possible_move, player)
            sim_score = self.minimax (state, other_player)  # simulate a game after making that move

            # undo move
            state.board[possible_move] = ' '
            state.current_winner = None
            sim_score['position'] = possible_move  # this represents the move optimal next move

            if player == max_player:  # X is max player
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score
        return best