import math
import random


class AlphaBetaComputerPlayer:
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves())  # Choose a random move for the first move
        else:
            # Get the best move using minimax algorithm with alpha-beta pruning
            square = self.alphabeta(game, self.letter)['position']
        return square

    def alphabeta(self, state, player, alpha=-math.inf, beta=math.inf):
        max_player = self.letter  # Maximizing player
        other_player = 'O' if player == 'X' else 'X'  # Other player

        # Check if the previous move is a winner
        if state.current_winner == other_player:
            return {'position': None, 'score': 1 * (state.num_empty_squares() + 1) if other_player == max_player else -1 * (state.num_empty_squares() + 1)}
        elif not state.num_empty_squares():  # No empty squares left
            return {'position': None, 'score': 0}  # Game is a draw

        # Initialize the best move
        if player == max_player:
            best = {'position': None, 'score': -math.inf}  # Maximizing player
        else:
            best = {'position': None, 'score': math.inf}  # Minimizing player

        for possible_move in state.available_moves():
            state.make_move(possible_move, player)  # Try the move

            # Simulate a game after making the move
            sim_score = self.alphabeta(state, other_player, alpha, beta)  # Recursive call

            # Undo the move
            state.board[possible_move] = ' '
            state.current_winner = None
            sim_score['position'] = possible_move  # Update the position

            # Update the best move
            if player == max_player:  # Maximizing player
                if sim_score['score'] > best['score']:
                    best = sim_score
                alpha = max(alpha, best['score'])
            else:  # Minimizing player
                if sim_score['score'] < best['score']:
                    best = sim_score
                beta = min(beta, best['score'])

            if alpha >= beta:
                break

        return best
