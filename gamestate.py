'''

Name:         gamestate.py

Description:  Handles the game's logic and state

'''

#--------------#
#  Game State  #
#--------------#

gamestate = {
    # Board:
    'board': [0]*9,
    # Game running:
    'active': True
}

#--------------#
#    Pieces    #
#--------------#

# Sets the piece in the game state dictionary


def set_piece(y, x, piece):
    # potential coords
    position = [[4, 19], [4, 23], [4, 27], [6, 19], [6, 23],
                [6, 27], [8, 19], [8, 23], [8, 27]]
    for index, pos in enumerate(position):
        # Check if you can place the piece or if it's occupied
        if [y, x] == pos and gamestate['board'][index] is 0:
            gamestate['board'][index] = piece
            result = True
            break
        else:
            result = False
    return result


#------------------#
#    Win Combos    #
#------------------#
def win_combos():
    # Win combinations
    gs = gamestate['board']
    won = dict(enumerate(
        [(gs[0], gs[1], gs[2]),
         (gs[3], gs[4], gs[5]),
         (gs[6], gs[7], gs[8]),
         (gs[0], gs[3], gs[6]),
         (gs[1], gs[4], gs[7]),
         (gs[2], gs[5], gs[8]),
         (gs[0], gs[4], gs[8]),
         (gs[2], gs[4], gs[6])]
    ))
    return won


#------------------#
#  Check for win   #
#------------------#

# Check for winning combination in gamestate_list
def win_check():
    won = win_combos()
    for combo in won.values():
        # Check for winner
        if 0 not in combo and len(set(combo)) is 1:
            result = combo[0]
            break
        # Check for tie
        elif 0 not in gamestate['board']:
            result = None
        else:
            result = False
    return result

# Idea: Test iteration by going through 0-8, if there's any 0s in those elements exclude them from a list.. find which character shows up the most and try to find a pair of 3 of that character matching a win combination


def end_game():
    gamestate['active'] = False
    return None


def restart():
    gamestate['board'] = [0]*9
    gamestate['active'] = True
    return True
