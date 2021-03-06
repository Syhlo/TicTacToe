'''

Name:          TicTacToe

Description:   TicTacToe using Curses for input and graphics

Author:        Syhlo

'''
import curses
from curses import wrapper
from itertools import cycle
import gamestate as gs


def main(stdscr):
    # Color sets
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)

    # Initial Parameters
    curses.noecho()

    #-------------------#
    #    Board Window   #
    #-------------------#

    board = curses.newwin(14, 46, 1, 5)

    def drawboard():
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

        # Content
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

        # Content
        hkm.addstr(1, 2, 'Movement Keys:')
        hkm.addstr(2, 3, '[WASD] [HJKL] [Arrow Keys]')
        hkm.addstr(4, 2, 'Quit:')
        hkm.addstr(5, 3, '[Shift + Q]')
        hkm.addstr(7, 2, 'Place Piece:')
        hkm.addstr(8, 3, '[Enter] [Space]')
        hkm.addstr(10, 2, 'Restart:')
        hkm.addstr(11, 3, '[Shift + R]')
        hkm.refresh()

    #--------------------#
    #   Hotkey Control   #
    #--------------------#

    def hotkeys():
        # Set cursor
        curses.curs_set(1)

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
                board.refresh()
                status.addstr(0, 1, '[ Turn: {}  ]'.format(track))
                status.refresh()
                get_winner()
            else:
                # Cycle back to the piece that you attempted to place
                tracker()
                pieces()

        # Check for winner
        def get_winner():
            winner = gs.win_check()

            # Found a winner
            if winner is str(winner):

                # Build winner prompt
                win = curses.newwin(3, 40, 11, 8)
                win.bkgd(' ', curses.color_pair(2))
                win.box()

                # Content
                win.addstr(
                    1, 2, '* Piece {} has won. Restart? Y/N    *'.format(winner))
                gs.end_game()

                # Call input controller
                prompt_input(win, 30)

            # Found a draw
            elif winner is None:
                gs.win_check()  # Verify there is no winner

                # Build draw prompt
                draw = curses.newwin(3, 40, 11, 8)

                # Settings
                draw.bkgd(' ', curses.color_pair(1))
                draw.box()

                # Content
                draw.addstr(1, 2, '* Ended in a draw. Restart? Y/N    *')
                draw.refresh()
                gs.end_game()

                # Call input controller
                prompt_input(draw, 30)

        #------------------#
        #  Prompt Hotkeys  #
        #------------------#

        def prompt_input(win_name, nx):
            while gs.GAMESTATE['active'] is False:
                # Position mouse and catch user input
                win_name.move(1, nx)
                ch = win_name.getch()

                # Movement [Keys: AD, HL, and Arrow Keys]
                if ch in (ord('a'), ord('h'), curses.KEY_LEFT) and nx > 30:
                    nx -= 2
                if ch in (ord('d'), ord('l'), curses.KEY_RIGHT) and nx < 31:
                    nx += 2

                # Selection [Keys: E or Spacebar]
                if ch in (ord('e'), ord(' ')):
                    if nx == 32:  # No
                        gs.GAMESTATE['close'] = True
                        break
                    if nx == 30:  # Yes
                        gs.restart()
                        board.clear()
                        drawboard()
                        break

                # Exit [Key: Shift + Q]
                if ch == ord('Q'):
                    break

        #-------------------#
        #      Hotkeys      #
        #-------------------#

        while gs.GAMESTATE['close'] is not True:
            # Settings
            board.move(y, x)
            c = board.getch()

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
