'''

Name:          TicTacToe

Description:   TicTacToe using Curses for input and graphics

Date:          Start: Nov 21 2018

Contributors:  Syhlo & Bippo123

'''
import curses as cs
import gamestate
from itertools import cycle
from curses import wrapper


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

        # Board Text
        b.addstr(0, 17, '[ TicTacToe ]')
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
        hk = cs.newwin(14, 31, 1, 52)
        hk.bkgd(' ', cs.color_pair(1))
        hk.box()
        hk.addstr(0, 8, '[ Hotkey Menu ]')
        hk.addstr(2, 2, 'Movement Keys:')
        hk.addstr(3, 3, '[WASD] [HJKL] [Arrow Keys]')
        hk.addstr(5, 2, 'Quit:')
        hk.addstr(6, 3, '[Shift + Q]')
        hk.addstr(8, 2, 'Place Piece:')
        hk.addstr(9, 3, '[Enter] [Space]')
        hk.addstr(11, 2, 'Restart:')
        hk.addstr(12, 3, '[Shift + R]')
        hk.refresh()

    #-------------------#
    #   Input Control   #
    #-------------------#
    # Set cursor
    cs.curs_set(1)

    # Hotkey Inputs
    def hotkeys():
        # cursor y,x coords
        y, x = 6, 23
        build = True
        piece = cycle('XO')
        while True:
            # Settings
            b.move(y, x)
            c = b.getch()

            #-------------------#
            #      Hotkeys      #
            #-------------------#

            # Key input [Keys: WASD, HJKL (VIM), and Arrow Keys]
            if c in (ord('w'), ord('k'), cs.KEY_UP) and y > 4:
                y -= 2
            elif c in (ord('s'), ord('j'), cs.KEY_DOWN) and y < 8:
                y += 2
            elif c in (ord('a'), ord('h'), cs.KEY_LEFT) and x > 19:
                x -= 4
            elif c in (ord('d'), ord('l'), cs.KEY_RIGHT) and x < 27:
                x += 4

            # Hotkey Menu [Key: M]
            elif c == ord('m'):
                hk = cs.newwin(14, 31, 1, 52)
                if build:
                    hotkey_menu()
                    build = False
                else:
                    hk.clear()
                    hk.refresh()
                    build = True

            # Place pieces [Keys: E or Spacebar]
            elif c in (ord('e'), ord(' ')):
                b.addch(y, x, next(piece))

            # Reset Board [Key: Shift + R]
            elif c == ord('R'):
                b.clear()
                drawboard()

            # Exit [Key: Shift + Q]
            elif c == ord('Q'):
                break

    hotkeys()


wrapper(main)

'''

TO DO:
Internet co-op ? ❌

Splash Page: ?
    - Start ❌
    - Options [Online/Offline, Port, Color Theme] ❌
    - About ❌

Status information:
    - Winner (p1 won/p2 won) ❌
    - Reload ❌
    - Playing ❌

Tie in game logic:
    - set_piece() ❌
    - tictactoe() ❌
    - win_check -> end_game() ❌
    - reset() ❌


'''
