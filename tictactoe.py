'''

Name:          TicTacToe

Description:   TicTacToe using Curses for input and graphics

Date:          Start: Nov 21 2018

Contributors:  Syhlo & Bippo123

Initialize everything in here
Flow: playerstate and board -> gamestate -> tictactoe (init file)

'''

# Import libraries

import curses as cs
import time
import gamestate
from curses import wrapper

''' 

TO DO:
Handle object placement ❌
Tie in game logic:
    - set_piece() ❌
    - tictactoe() ❌
    - win_check -> end_game() ❌
    - reset() ❌
Hotkeys:
    - Movement: WASD, HJKL, Arrow Keys ✔️
    - Select: Enter, Space ❌
    - Quit: Shift + Q ✔️
    - Menu: M  (Opens Hotkey Menu) ❌


'''


def main(stdscr):

    # Color sets
    cs.init_pair(1, cs.COLOR_WHITE, cs.COLOR_BLACK)  # bg,fg
    cs.init_pair(2, cs.COLOR_YELLOW, cs.COLOR_BLACK)

    #-------------------#
    #    Body Window    #
    #-------------------#
    b = cs.newwin(14, 46, 0, 5)
    b.bkgd(' ', cs.color_pair(1))
    b.box()
    b.keypad(True)

    # Initial Parameters
    cs.noecho()

    # not in use:
    # cols, rows = b.getmaxyx()
    # 14      46

    def drawboard():
        #-------------------#
        #  TicTacToe Board  #
        #-------------------#
        # Board Horizontal Lines
        b.hline(5, 18, cs.ACS_HLINE | cs.A_PROTECT, 11)
        b.hline(7, 18, cs.ACS_HLINE, 11)

        # Board Vertical Lines
        b.vline(4, 21, cs.ACS_VLINE, 5)
        b.vline(4, 25, cs.ACS_VLINE, 5)

        # Body Combining Lines
        b.vline(5, 21, cs.ACS_SSSS, 1)
        b.vline(5, 25, cs.ACS_SSSS, 1)
        b.vline(7, 21, cs.ACS_SSSS, 1)
        b.vline(7, 25, cs.ACS_SSSS, 1)
    drawboard()

    #-------------------#
    #   Status Window   #
    #-------------------#
    s = cs.newwin(1, 40, 14, 8)
    s.bkgd(' ', cs.color_pair(1))
    s.box()

    # Status Bar Text
    def status_bar():
        s.addstr(0, 1,  '[ turn: p1 ]')
        s.addstr(0, 27, '[  status  ]')
    status_bar()

    # Refresh
    b.refresh()
    s.refresh()

    #-------------------#
    #  Cursor Control   #
    #-------------------#
    # Set cursor
    cs.curs_set(1)

    # Cursor Input
    def curs():
        y, x = 6, 23
        c = None
        b.move(6, 23)
        while True:
            b.move(y, x)
            b.refresh()
            c = b.getch()

            # Key input [WASD keys]
            if c in (ord('w'), ord('k'), cs.KEY_UP) and y > 4:
                y -= 2
            elif c in (ord('s'), ord('j'), cs.KEY_DOWN) and y < 8:
                y += 2
            elif c in (ord('a'), ord('h'), cs.KEY_LEFT) and x > 19:
                x -= 4
            elif c in (ord('d'), ord('l'), cs.KEY_RIGHT) and x < 27:
                x += 4

            # Place pieces with E or SpaceBar
            elif c in (ord('e'), ord(' ')):
                pass

            # If Shift + Q exit the program
            elif c == ord('Q'):
                break

    curs()


wrapper(main)
