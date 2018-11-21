'''

Name:       gamestate.py 

TicTacToe:
    - Handle game logic in a while loop
        - Check if winner after every placement (run win check)
        - Place piece (X or O) depending on playerstate (check playerstate, call board placement method)
        - Disable piece placement in occupied spaces (if index item is not 0 don't place? send improper move warning?)

Win Check:
    - Scan dict.list left to right (*[0]-[2])
    - Scan dict.list top to bottom (top[x] middle[x] bottom[x])
    - Scan dict.list diagonally (top[0] middle[1] bottom[3] and 3,1,0 as well)
    - If there's three in a row get the winner and pass it to end game

Note: Maybe concatenate the lists and iterate over that one list for possible win positions?

End Game:
    - Print message stating who won
    - Ask if they would like to play again (if yes, reset. if no, exit.)

Reset:
    - Reset all data structures (reassign to original values)
    - Reset board
    - Reset while loop (run tictactoe())

Set Piece:
    - Change gamestate.board.<key>.<value>[x] to piece
    - Update playerstate.turn.<value>

'''

# Import libraries
import board

# Gamestate dictionary
gamestate = {'board': {
    (1, 2, 3): ['0', '0', '0'],
    (4, 5, 6): ['0', '0', '0'],
    (7, 8, 9): ['0', '0', '0']
},
    'active': 'True'
}

# Playerstate dictionary
playerstate = {
    'turn': 1,  # 1 or 2
    'player1': 'X',
    'player2': 'O'
}


def tictactoe():
    pass


def set_piece(player):
    pass


def win_check(state):
    pass


def end_game(winner):
    pass


def reset():
    pass
