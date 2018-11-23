'''
Name:          TicTacToe

Description:   TicTacToe using Curses for input and graphics

Date:          Start: Nov 21 2018

Contributors:  Syhlo & Bippo123

'''

# Import libraries

import curses as cs
import gamestate
from itertools import cycle
from curses import wrapper

'''

TO DO:
Internet co-op ? ❌

Splash Page: ?
    - Start ❌
    - Options [Port, Online/Offline, Color Theme] ❌
    - Rules ❌
    - About ❌

Status information:
    - Winner (p1 won/p2 won) ❌
    - Reload ❌
    - Playing ❌

Handle piece placement
    - Cycle between X and O ❌

Tie in game logic:
    - set_piece() ❌
    - tictactoe() ❌
    - win_check -> end_game() ❌
    - reset() ❌


'''


def main(stdscr):

    # Color set
    cs.init_pair(1, cs.COLOR_WHITE, cs.COLOR_BLACK)  # bg,fg

    #-------------------#
    #    Board Window   #
    #-------------------#
    b = cs.newwin(14, 46, 1, 5)
    b.keypad(True)

    # Initial Parameters
    cs.noecho()  # no keyboard echo
    cs.cbreak()  # don't wait for newline

    # not in use (yet):
    # cols, rows = b.getmaxyx()
    # 14      46

    def drawboard():
        # Settings
        b.bkgd(' ', cs.color_pair(1))
        b.box()
        b.addstr(1, 35, '[Keys: M]')

        #-------------------#
        #  TicTacToe Board  #
        #-------------------#
        # Board Horizontal Lines
        b.hline(5, 18, cs.ACS_HLINE, 11)
        b.hline(7, 18, cs.ACS_HLINE, 11)

        # Board Vertical Lines
        b.vline(4, 21, cs.ACS_VLINE, 5)
        b.vline(4, 25, cs.ACS_VLINE, 5)

        # Board Combining Lines
        b.vline(5, 21, cs.ACS_SSSS, 1)
        b.vline(5, 25, cs.ACS_SSSS, 1)
        b.vline(7, 21, cs.ACS_SSSS, 1)
        b.vline(7, 25, cs.ACS_SSSS, 1)
    drawboard()

    #-------------------#
    #   Status Window   #
    #-------------------#
    s = cs.newwin(1, 40, 15, 8)
    s.bkgd(' ', cs.color_pair(1))
    s.box()

    # Status Bar Contents
    def status_bar():
        # Status Text
        s.addstr(0, 1,  '[ turn: p1 ]')
        s.addstr(0, 27, '[  status  ]')
    status_bar()

    # Refresh
    b.refresh()
    s.refresh()

    #-------------------#
    #   Hotkey Window   #
    #-------------------#
    def hotkey_menu():
        hk = cs.newwin(13, 31, 1, 52)
        hk.bkgd(' ', cs.color_pair(1))
        hk.box()
        hk.addstr(1, 2, 'Movement Keys:')
        hk.addstr(2, 3, '[WASD] [HJKL] [Arrow Keys]')
        hk.addstr(4, 2, 'Quit:')
        hk.addstr(5, 3, '[Shift + Q]')
        hk.addstr(7, 2, 'Place Piece:')
        hk.addstr(8, 3, '[Enter] [Space]')
        hk.addstr(10, 2, 'Restart:')
        hk.addstr(11, 3, '[Shift + R]')
        hk.refresh()

    #-------------------#
    #  Cursor Control   #
    #-------------------#
    # Set cursor
    cs.curs_set(1)

    # Cursor Input
    def hotkeys():
        y, x = 6, 23
        c = None
        b.move(6, 23)
        while True:
            # Settings
            b.move(y, x)
            b.refresh()
            c = b.getch()

            # Cycle pieces (Not Working)
            piece = cycle('XO')

            #-------------------#
            #      Hotkeys      #
            #-------------------#

            # Key input [WASD keys]
            if c in (ord('w'), ord('k'), cs.KEY_UP) and y > 4:
                y -= 2
            elif c in (ord('s'), ord('j'), cs.KEY_DOWN) and y < 8:
                y += 2
            elif c in (ord('a'), ord('h'), cs.KEY_LEFT) and x > 19:
                x -= 4
            elif c in (ord('d'), ord('l'), cs.KEY_RIGHT) and x < 27:
                x += 4

            # Hotkey Menu
            elif c == ord('m'):
                hotkey_menu()
                b.move(y, x)

            # Place pieces with E or SpaceBar
            elif c in (ord('e'), ord(' ')):
                b.addch(y, x, next(piece))

            # If Shift + R reset board
            elif c == ord('R'):
                b.clear()
                drawboard()

            # If Shift + Q exit the program
            elif c == ord('Q'):
                break

    hotkeys()


wrapper(main)
