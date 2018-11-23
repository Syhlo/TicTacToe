'''

Name:         gamestate.py 

Description:  Handles game logic, game state, and player state

'''

#--------------#
#  Game State  #
#--------------#

gamestate = {'board': {
    'top':    ['1', '2', '3'],
    'middle': ['4', '5', '6'],
    'bottom': ['7', '8', '9']
},
    'board_active': 'False'
}

#----------------#
#  Player State  #
#----------------#

playerstate = {
    'turn': 1,  # 1 or 2
    'player1': 'X',
    'player2': 'O'
}


# Main loop
def tictactoe():
    '''
    Logic:
        - Handle game logic in a while loop
            - Check if winner after every placement (run win check)
            - Place piece (X or O) depending on playerstate (check playerstate, call board placement method)
            - Disable piece placement in occupied spaces (if index item is not 0 don't place? send improper move warning?)
    '''
    pass


# Sets the piece in the game state dictionary
def set_piece(y, x, player):
    # Tool to find the key and index
    gamestate_key = {
        '4': 'top',
        '6': 'middle',
        '8': 'bottom',
        '19': 0,
        '23': 1,
        '27': 2
    }

    # Return key associated with y
    key = gamestate_key[str(y)]
    # Return index associated with x
    index = gamestate_key[str(x)]

    # Set the proper list[index] to the player's piece
    gamestate['board'][key][index] = playerstate[str(player)]

    # testing purposes
    print(gamestate['board'])


# Check if working
set_piece(4, 27, 'player1')


# Create a list of the board state and return it
def concatenate():
    gamestate_list = []
    for value in gamestate['board'].values():
        gamestate_list.extend(value)
    return gamestate_list


# Check for winner
def win_check(state):
    iterate = concatenate()
    # Possible win combinations (concatenated list indices)
    # [0][1][2] [3][4][5] [6][7][8]
    # [0][3][6] [1][4][7] [2][5][8]
    # [0][4][8] [2][4][6]

    '''
    Logic:
        - Iterate local list cross referencing win combinations (dictionary ?)
        - For win combinations not containing '0': len(set(<combination>))
        - Result is equal to 1 (all 3 are the same)? Determine who won and call end_game(<winner>)
    '''
    pass


# End game and offer reset
def end_game(winner):
    '''
    Logic:
        - Toggle gamestate['active'] to 'False' (cancels tictactoe() while loop)
        - Display message stating who won
        - Ask if they would like to play again (Yes -> Reset, No -> Exit program)
    '''
    pass


# Reset game state, player state, and the board
def reset():
    '''
    Logic:
        - Reset all data structures (reassign to original values)
        - Reset board
        - Reset while loop(run tictactoe())
    '''
    pass
