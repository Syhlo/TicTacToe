'''

Name:       gamestate.py 

TicTacToe:
    - Handle game logic in a while loop
        - Check if won after every placement (run win check)
        - Place objects (X or O) depending on playerstate (check playerstate)
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

'''

import playerstate

gamestate = True
