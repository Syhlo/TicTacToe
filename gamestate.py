'''

Name:       gamestate.py 

TicTacToe:
    - Handle game logic in a while loop
        - Check if winner after every placement (run win check)
        - Place piece (X or O) depending on playerstate (check playerstate, call board placement method)
        - Disable piece placement in occupied spaces (if index item is not 0 don't place? send improper move warning?)

Win Check:
    - Concatenate board state lists into one ✔️
    - Iterate over list for possible win combinations
    - If there's a winner get the winner and pass it to end game

End Game:
    - Toggle gamestate[active] to 'False' (cancel while loop)
    - Display message stating who won
    - Ask if they would like to play again (Yes -> Reset, No -> Exit program)

Reset:
    - Reset all data structures (reassign to original values)
    - Reset board
    - Reset while loop (run tictactoe())

Set Piece:
    - Change gamestate['board']['<key>'][<value>][index] to placed piece
    - Update playerstate.turn.<value>

'''

# Import libraries
import board


#--------------#
#  Game State  #
#--------------#

gamestate = {'board': {
    'top':    ['0', '0', '0'],
    'middle': ['0', '0', '0'],
    'bottom': ['0', '0', '0']
},
    'active': 'False'
}

#----------------#
#  Player State  #
#----------------#

playerstate = {
    'turn': 1,  # 1 or 2
    'player1': 'X',
    'player2': 'O'
}


def tictactoe():
    pass


def set_piece(player):
    pass


# Create a list of the board state and return it
def concatenate():
    gamestate_list = []
    for value in gamestate['board'].values():
        gamestate_list.extend(value)
    return gamestate_list


def win_check(state):
    iterate = concatenate()
    # Possible win indexes with concatenated list:
    # [0][1][2] [3][4][5] [6][7][8]
    # [0][3][6] [1][4][7] [2][5][8]
    # [0][4][8] [2][4][6]
    pass


def end_game(winner):
    pass


def reset():
    pass
