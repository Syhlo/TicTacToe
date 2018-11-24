'''

Name:         gamestate.py

Description:  Handles the game's logic and state

'''

#--------------#
#  Game State  #
#--------------#
# Handles the state of the game
gamestate = {'board': {
    'top':    [0, 0, 0],
    'middle': [0, 0, 0],
    'bottom': [0, 0, 0]
},
    # True = Game Running, False = Game Not Running
    'board_active': True
}


# Sets the piece in the game state dictionary
def set_piece(y, x, piece):
    # Tool to find the key and index in gamestate dictionary based off of coordinates
    gamestate_key = {
        '4': 'top',
        '6': 'middle',
        '8': 'bottom',
        '19': 0,
        '23': 1,
        '27': 2
    }

    # Return key (list) associated with y coordinate
    key = gamestate_key[str(y)]

    # Return value (index of list) associated with x coordinate
    index = gamestate_key[str(x)]

    # If the value is 0 place the piece otherwise return False (unable to place)
    if gamestate['board'][key][index] is 0:
        # Set the piece in gamestate's board
        gamestate['board'][key][index] = piece
        return True  # Success, set piece in curses' board
    else:
        return False  # Failure, do not set piece on either board


# Create a combined list of all lists in gamestate['board'] and return it for use
def concatenate():
    gamestate_list = []
    for value in gamestate['board'].values():
        gamestate_list.extend(value)
    return gamestate_list


# Check for winning win_combo in gamestate_list
def win_check():
    # Create lgamestate_list
    gl = concatenate()

    # gl = [1, 1, 0, 0, 2, 1, 1, 2, 2]

    # List of tuples containing possible win win_combo
    win_combo = [(gl[0], gl[1], gl[2]),
                 (gl[3], gl[4], gl[5]),
                 (gl[6], gl[7], gl[8]),
                 (gl[0], gl[3], gl[6]),
                 (gl[1], gl[4], gl[7]),
                 (gl[2], gl[5], gl[8]),
                 (gl[0], gl[4], gl[8]),
                 (gl[2], gl[4], gl[6]), ]

    # incrementer
    i = 0
    while i <= len(win_combo)-1:

        # If no winner
        if 0 not in gl:
            # print('No winner')
            return None
        # If the combination does not contain 0s
        elif 0 not in win_combo[i]:

            # If the combination is 1 = winner
            if len(set(win_combo[i])) is 1:
                # First item of the winning tuple (piece)
                winner = win_combo[i][0]
                return winner

            # If the combination is more than 1 = continue
            elif len(set(win_combo[i])) > 1:
                i += 1

        # If there is a 0 in the combination pass
        else:
            i += 1
    return False

# End game and offer restart


def end_game():
    '''
    Logical steps:
        - Toggle gamestate['board_active'] to 'False' (this will cancel curses active while loop)
    '''
    pass


# Restart the game state
def restart():
    '''
    Logical steps:
        - Reset gameboard dictionary (reassign the original dictionary to var gameboard)

        - toggle gamestate[board_active] back to 'True'
    '''
    return True
