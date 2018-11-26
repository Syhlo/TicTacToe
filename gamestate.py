'''

Name:         GAMESTATE.py

Description:  Handles the game's logic and state

'''

GAMESTATE = {
    # Board:
    'board': [0]*9,
    # Game running:
    'active': True
}


# Sets the piece in the game state dictionary
def set_piece(y, x, piece):
    # Potential coords
    positions = [[4, 19], [4, 23], [4, 27], [6, 19], [6, 23],
                 [6, 27], [8, 19], [8, 23], [8, 27]]
    for index, pos in enumerate(positions):
        # Check if you can place the piece or if it's occupied
        if [y, x] == pos and GAMESTATE['board'][index] is 0:
            GAMESTATE['board'][index] = piece
            result = True
            break
        else:
            result = False
    return result


# Win combination check
def win_combos():
    gs_ = GAMESTATE['board']
    won = dict(enumerate(
        [(gs_[0], gs_[1], gs_[2]), (gs_[3], gs_[4], gs_[5]),
         (gs_[6], gs_[7], gs_[8]), (gs_[0], gs_[3], gs_[6]),
         (gs_[1], gs_[4], gs_[7]), (gs_[2], gs_[5], gs_[8]),
         (gs_[0], gs_[4], gs_[8]), (gs_[2], gs_[4], gs_[6])]
    ))
    return won


# Check for win or draw
def win_check():
    for combo in win_combos().values():
        # Check for winner
        if 0 not in combo and len(set(combo)) is 1:
            result = combo[0]
            break
        # Check for tie
        elif 0 not in GAMESTATE['board']:
            result = None
        else:
            result = False
    return result


def end_game():
    GAMESTATE['active'] = False
    return None


def restart():
    GAMESTATE['board'] = [0]*9
    GAMESTATE['active'] = True
    return True
