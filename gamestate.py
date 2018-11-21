'''

Name:       gamestate.py 

TicTacToe:
    - Handle game logic in a while loop
        - Check if won after every placement (run win check)
        - Place objects (X or O) depending on playerstate (check playerstate, call board placement method)
        - Disable object placement in occupied spaces (if index item is not 0 don't place? send improper move warning?)

Win Check:
    - Scan dict.list left to right (*[0]-[2])
    - Scan dict.list top to bottom (top[x] middle[x] bottom[x])
    - Scan dict.list diagonally (top[0] middle[1] bottom[3] and 3,1,0 as well)
    - If there's three in a row get the winner and pass it to end game

End Game:
    - Print message stating who won
    - Ask if they would like to play again (if yes, reset. if no, exit.)

Reset:
    - Reset all data structures (reassign to original values)
    - Reset board
    - Reset while loop (run tictactoe())

Note: Perhaps store the board state as such: 
    {
        (0,1,2):['o','x','x'],
        (3,4,5):['o','o','x'],
        (6,7,8):['x','x','o']
    }

'''

# Import libraries
import playerstate as ps
import board as pb

# If game has ended or not
gamestate = None


def tictactoe():
    pass


def win_check():
    pass


def end_game():
    pass


def reset():
    pass
