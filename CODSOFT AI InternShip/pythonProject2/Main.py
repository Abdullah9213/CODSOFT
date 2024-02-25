from Human_Player import HumanPlayer
from Computer_Player import AlphaBetaComputerPlayer
from TIC_TAC_TOE import TicTacToe, play

if __name__ == '__main__':
    X_player = HumanPlayer('X')
    O_player = AlphaBetaComputerPlayer('O')  # Used Minimax Algorithm enhanced by AlphaBeta pruning for computer player
    TTT = TicTacToe()
    play(TTT, X_player, O_player)
