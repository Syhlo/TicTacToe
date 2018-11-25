'''

Name:          TicTacToe

Description:   TicTacToe using Curses for input and graphics

Date:          Start: Nov 21 2018

Author:        Syhlo

'''
import curses as cs
import gamestate as gs
from itertools import cycle
from curses import wrapper

# testing purposes
print(gs.gamestate['board'])


def main(stdscr):

    # Color sets
    cs.init_pair(1, cs.COLOR_BLUE, cs.COLOR_BLACK)  # bg,fg

    # Initial Parameters
    cs.noecho()
    cs.raw()
    cs.cbreak()  # no keyboard echo

    #-------------------#
    #    Board Window   #
    #-------------------#

    b = cs.newwin(14, 46, 1, 5)
    b.keypad(True)

    # not in use (yet):
    # cols, rows = b.getmaxyx()
    # 14      46

    def drawboard():
        # Settings
        b.box()

        # Board Text
        b.addstr(0, 17, '[ TicTacToe ]')

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
        b.refresh()
    drawboard()

    #-------------------#
    #   Status Window   #
    #-------------------#

    s = cs.newwin(1, 40, 15, 8)
    s.box()

    # Status Bar Contents
    def status_bar():
        s.addstr(0, 1,  '[ Turn: X  ]')
        s.addstr(0, 27, '[ HKeys: M ]')
        s.refresh()
    status_bar()

    #-------------------#
    #   Hotkey Window   #
    #-------------------#

    def hotkey_menu():
        hk = cs.newwin(14, 31, 1, 52)
        hk.box()
        hk.addstr(0, 8, '[ Hotkey Menu ]')
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
    #   Input Control   #
    #-------------------#

    # Set cursor & y,x
    cs.curs_set(1)

    # Hotkey Control
    def hotkeys():
        # cursor y,x coords
        y, x = 6, 23

        # Whether the hotkeys menu is showing
        hk_showing = True
        pieces = cycle('XO').__next__
        tracker = cycle('OX').__next__

        #--------------------#
        #  Hotkey Functions  #
        #--------------------#

        # Handles placement of pieces
        def place_piece():
            # Get which piece to place and next piece to place
            piece = pieces()
            track = tracker()

            # Attempt to place it on the gamestate board
            can_place = gs.set_piece(y, x, piece)
            print(can_place)

            # If you can place it on the gamestate board render it
            if can_place:
                s.addstr(0, 1,  '[ Turn: {}  ]'.format(track))
                b.addch(y, x, piece)
                s.refresh()

            else:
                # If you can't place the piece then cycle back to the piece
                # you attempted to place
                tracker()
                pieces()

        def get_winner():
            winner = gs.win_check()

            # If there's a tie
            if winner is None:
                # Place the last piece and check for win
                place_piece()
                gs.win_check()

                # Build window
                tie = cs.newwin(3, 40, 11, 8)
                tie.bkgd(' ', cs.color_pair(1))
                tie.box()
                tie.addstr(1, 2, '* Ended in a tie. Restart? Y/N    *')
                tie.refresh()
                nx = 30

                # Start tie window's input loop
                while True:
                    # Position mouse and catch user input
                    tie.move(1, nx)
                    ch = tie.getch()

                    # Movement [Keys: AD, HL, and Arrow Keys]
                    if ch in (ord('a'), ord('h'), cs.KEY_LEFT) and nx > 30:
                        nx -= 2
                    if ch in (ord('d'), ord('l'), cs.KEY_RIGHT) and nx < 31:
                        nx += 2

                    # Selection [Keys: E or Spacebar]
                    if ch in (ord('e'), ord(' ')):
                        if nx == 32:
                            pass
                        if nx == 30:
                            gs.restart()
                            b.clear()
                            drawboard()
                            break

                    # Exit [Key: Shift + Q]
                    if ch == ord('Q'):
                        break

            # No winner found
            elif winner is False:
                pass

            # Found winner
            elif winner is winner:
                s.addstr(0, 27, '[  {} WINS  ]'.format(winner))
                s.refresh()
                gs.end_game()

        #-------------------#
        #  Main Input Loop  #
        #-------------------#

        # Start main input loop
        while True:
            # Settings
            b.move(y, x)
            c = b.getch()

            #-------------------#
            #      Hotkeys      #
            #-------------------#

            # Movement [Keys: WASD, HJKL, and Arrow Keys]
            if c in (ord('w'), ord('k'), cs.KEY_UP) and y > 4:
                y -= 2
            if c in (ord('s'), ord('j'), cs.KEY_DOWN) and y < 8:
                y += 2
            if c in (ord('a'), ord('h'), cs.KEY_LEFT) and x > 19:
                x -= 4
            if c in (ord('d'), ord('l'), cs.KEY_RIGHT) and x < 27:
                x += 4

            # Hotkey Menu [Key: M]
            if c == ord('m'):
                hk = cs.newwin(14, 31, 1, 52)
                if hk_showing:
                    hotkey_menu()
                    hk_showing = False
                else:
                    hk.clear()
                    hk.refresh()
                    hk_showing = True

            # Place pieces [Keys: E or Spacebar]
            if c in (ord('e'), ord(' ')):
                if gs.gamestate['board_active'] is True:
                    place_piece()
                    get_winner()

            # Restart Game [Key: Shift + R]
            if c == ord('R'):
                gs.restart()
                b.clear()
                drawboard()
                status_bar()

            # Exit [Key: Shift + Q]
            if c == ord('Q'):
                break
    hotkeys()


wrapper(main)

# testing purposes
print(gs.gamestate['board'])
print(gs.gamestate['board_active'])

'''

TO DO:
co-op ? ❌

Splash Page: ?
    - Start ❌
    - Options [Online/Offline, Port, Color Theme] ❌
    - About ❌
    - Exit ❌

BUGS:
Not placing last item during tie. Look at place_piece() and get_winner() to figure it out.
    Observations:
    - Item does not render until tie input loop is broken.
    - Item returns 'do not place' in set_piece()
    - It seems to be setting the piece in gamestate['board'] despite that.

'''
