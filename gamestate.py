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


#--------------#
#    Pieces    #
#--------------#

# Sets the piece in the game state dictionary
def set_piece(y, x, piece):
    # Plug a number into this and get a response
    gamestate_key = {
        # Possible Y coords
        '4': 'top',
        '6': 'middle',
        '8': 'bottom',

        # Possible X coords
        '19': 0,
        '23': 1,
        '27': 2
    }

    # Gives you the y coordinate responses (top, middle, bottom)
    key = gamestate_key[str(y)]

    # Gives you the x coordinate responses (0,1,2 - indices)
    index = gamestate_key[str(x)]

    # If the value is 0 place the piece otherwise return failure to place
    if gamestate['board'][key][index] is 0:
        gamestate['board'][key][index] = piece
        return True  # Success, set piece in curses' board
    else:
        return False  # Failure, do not set piece on either board


#------------------#
#  Check for win   #
#------------------#

# Create an extended list from the lists in gamestate['board'] and return it for use
def concatenate():
    gamestate_list = []
    for value in gamestate['board'].values():
        gamestate_list.extend(value)
    return gamestate_list


# Check for winning combination in gamestate_list
def win_check():
    # Get returned gamestate_list
    gl = concatenate()
    # gl = [1, 1, 1, 1, 1, 1, 1, 1, 1]

    # List of tuples containing possible combinations
    win_combo = [(gl[0], gl[1], gl[2]),
                 (gl[3], gl[4], gl[5]),
                 (gl[6], gl[7], gl[8]),
                 (gl[0], gl[3], gl[6]),
                 (gl[1], gl[4], gl[7]),
                 (gl[2], gl[5], gl[8]),
                 (gl[0], gl[4], gl[8]),
                 (gl[2], gl[4], gl[6]), ]

    # Iterate for winner
    i = 0
    while i <= len(win_combo)-1:
        # If the combo does not contain placeholders check for possible winner
        if 0 not in win_combo[i]:
            if len(set(win_combo[i])) is 1:
                # Get the element to use as winner character
                winner = win_combo[i][0]
                return winner

            # If the combo is not a winner then check next one
            elif len(set(win_combo[i])) > 1:
                i += 1

        # If there is a placeholder in the combo then increment
        else:
            i += 1

    # If all pieces are placed and no winner it must be a draw
    else:
        if 0 not in gl:
            return None

    # No winner or draw found
    return False

# Test iteration by going through 0-8, if there's any 0s in those elements exclude them from a list.. find which character shows up the most and try to find a pair of 3 of that character matching a win combination


# End game and offer restart
def end_game():
    gamestate['board_active'] = False
    return True


# Restart the game state
def restart():
    gamestate['board'] = {
        'top':    [0, 0, 0],
        'middle': [0, 0, 0],
        'bottom': [0, 0, 0]
    }
    gamestate['board_active'] = True
    return True
