'''

Name:          TicTacToe

Description:   TicTacToe using Curses for input and graphics

Date:          Start: Nov 21 2018

Author:        Syhlo

'''
import curses
from curses import wrapper
from itertools import cycle
import gamestate as gs


def main(stdscr):
    # Color sets
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)  # bg,fg

    # Initial Parameters
    curses.noecho()  # no keyboard echo

    #-------------------#
    #    Board Window   #
    #-------------------#
    board = curses.newwin(14, 46, 1, 5)

    def drawboard():
        # Settings
        board.box()
        board.keypad(True)

        # Board Title
        board.addstr(0, 17, '[ TicTacToe ]')

        #-------------------#
        #  TicTacToe Board  #
        #-------------------#

        # Board Horizontal Lines
        board.hline(5, 18, curses.ACS_HLINE, 11)
        board.hline(7, 18, curses.ACS_HLINE, 11)

        # Board Vertical Lines
        board.vline(4, 21, curses.ACS_VLINE, 5)
        board.vline(4, 25, curses.ACS_VLINE, 5)

        # Board Combining Lines
        board.vline(5, 21, curses.ACS_SSSS, 1)
        board.vline(5, 25, curses.ACS_SSSS, 1)
        board.vline(7, 21, curses.ACS_SSSS, 1)
        board.vline(7, 25, curses.ACS_SSSS, 1)
        board.refresh()
    drawboard()

    #-------------------#
    #   Status Window   #
    #-------------------#
    status = curses.newwin(1, 40, 15, 8)

    def status_bar():
        status.box()
        status.addstr(0, 1,  '[ Turn: X  ]')
        status.addstr(0, 27, '[ HKeys: M ]')
        status.refresh()
    status_bar()

    #-------------------#
    #   Hotkey Window   #
    #-------------------#
    hkm = curses.newwin(14, 31, 1, 52)

    def hotkey_menu():
        hkm.box()
        # Hotkey Menu Title
        hkm.addstr(0, 8, '[ Hotkey Menu ]')
        # Contents
        hkm.addstr(1, 2, 'Movement Keys:')
        hkm.addstr(2, 3, '[WASD] [HJKL] [Arrow Keys]')
        hkm.addstr(4, 2, 'Quit:')
        hkm.addstr(5, 3, '[Shift + Q]')
        hkm.addstr(7, 2, 'Place Piece:')
        hkm.addstr(8, 3, '[Enter] [Space]')
        hkm.addstr(10, 2, 'Restart:')
        hkm.addstr(11, 3, '[Shift + R]')
        hkm.refresh()

    #-------------------#
    #   Input Control   #
    #-------------------#

    # Set cursor
    curses.curs_set(1)

    # Hotkey Control
    def hotkeys():
        # Cursor y,x coords
        y, x = 6, 23

        # Whether the hotkeys menu is showing
        hk_showing = True

        # Pieces & next to move tracker
        pieces = cycle('XO').__next__
        tracker = cycle('OX').__next__

        #--------------------#
        #  Hotkey Functions  #
        #--------------------#

        # Handles placement of pieces
        def place_piece():
            # Get which piece to place and next move tracker
            piece = pieces()
            track = tracker()

            # Attempt to place it on the board
            can_place = gs.set_piece(y, x, piece)

            # If you can place it then render it
            if can_place:
                board.addch(y, x, piece)
                status.addstr(0, 1, '[ Turn: {}  ]'.format(track))
                status.refresh()
                get_winner()
            else:
                # Cycle back to the piece that you attempted to place
                tracker()
                pieces()

        def get_winner():
            winner = gs.win_check()

            # Found winner
            if winner is str(winner):
                status.addstr(0, 27, '[  {} WINS  ]'.format(winner))
                status.refresh()
                gs.end_game()

            # Found a draw
            elif winner is None:
                gs.win_check()  # Verify there is no winner

                # Build draw prompt
                draw = curses.newwin(3, 40, 11, 8)
                draw.bkgd(' ', curses.color_pair(1))
                draw.box()
                draw.addstr(1, 2, '* Ended in a draw. Restart? Y/N    *')
                draw.refresh()
                nx = 30
                gs.end_game()

                #-------------------#
                #  Draw Input Loop  #
                #-------------------#

                while gs.GAMESTATE['active'] is False:
                    # Position mouse and catch user input
                    draw.move(1, nx)
                    ch = draw.getch()

                    # Movement [Keys: AD, HL, and Arrow Keys]
                    if ch in (ord('a'), ord('h'), curses.KEY_LEFT) and nx > 30:
                        nx -= 2
                    if ch in (ord('d'), ord('l'), curses.KEY_RIGHT) and nx < 31:
                        nx += 2

                    # Selection [Keys: E or Spacebar]
                    if ch in (ord('e'), ord(' ')):
                        if nx == 32:  # No
                            pass
                        if nx == 30:  # Yes
                            gs.restart()
                            board.clear()
                            drawboard()
                            break

                    # Exit [Key: Shift + Q]
                    if ch == ord('Q'):
                        break

        #-------------------#
        #  Main Input Loop  #
        #-------------------#

        while gs.GAMESTATE['active']:
            # Settings
            board.move(y, x)
            c = board.getch()

            #-------------------#
            #      Hotkeys      #
            #-------------------#

            # Movement [Keys: WASD, HJKL, and Arrow Keys]
            if c in (ord('w'), ord('k'), curses.KEY_UP) and y > 4:
                y -= 2
            if c in (ord('s'), ord('j'), curses.KEY_DOWN) and y < 8:
                y += 2
            if c in (ord('a'), ord('h'), curses.KEY_LEFT) and x > 19:
                x -= 4
            if c in (ord('d'), ord('l'), curses.KEY_RIGHT) and x < 27:
                x += 4

            # Hotkey Menu [Key: M]
            if c == ord('m'):
                hkm = curses.newwin(14, 31, 1, 52)
                if hk_showing:
                    hotkey_menu()
                    hk_showing = False
                else:
                    hkm.clear()
                    hkm.refresh()
                    hk_showing = True

            # Place pieces [Keys: E or Spacebar]
            if c in (ord('e'), ord(' ')):
                if gs.GAMESTATE['active'] is True:
                    place_piece()

            # Restart Game [Key: Shift + R]
            if c == ord('R'):
                gs.restart()
                board.clear()
                drawboard()
                status_bar()

            # Exit [Key: Shift + Q]
            if c == ord('Q'):
                break
    hotkeys()


wrapper(main)
