'''

Name:          TicTacToe

Description:   TicTacToe using Curses for input and graphics

Date:          Start: Nov 21 2018

Author:  Syhlo

'''
import curses as cs
import gamestate as gs
from itertools import cycle
from curses import wrapper

# testing purposes
print(gs.gamestate['board'])


def main(stdscr):

    # Color set
    cs.init_pair(1, cs.COLOR_RED, cs.COLOR_BLACK)  # bg,fg

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
    drawboard()

    #-------------------#
    #   Status Window   #
    #-------------------#
    s = cs.newwin(1, 40, 15, 8)
    s.box()

    # Status Bar Contents
    def status_bar():
        # Status Text
        s.addstr(0, 1,  '[ Turn: X  ]')
        s.addstr(0, 27, '[ HKeys: M ]')
    status_bar()

    # Refresh
    b.refresh()
    s.refresh()

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
    # Set cursor
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

        # Piece placing logic
        def place_piece():
            # Get which piece to place
            piece = pieces()
            track = tracker()

            # Run set_piece() to try to place it on the board
            can_place = gs.set_piece(y, x, piece)

            # If place_piece is true (it can be placed
            if can_place:
                s.addstr(0, 1,  '[ Turn: {}  ]'.format(track))
                b.addch(y, x, piece)
                s.refresh()

            else:
                # Run pieces() again to prevent repeated pieces
                tracker()
                pieces()
                pass

        def get_winner():
            winner = gs.win_check()

            if winner is None:
                nowin = cs.newwin(3, 40, 11, 8)
                nowin.bkgd(' ', cs.color_pair(1))
                nowin.box()
                nowin.addstr(
                    1, 2, '* Ended in a draw. Restart? Y/N    *')
                nowin.refresh()
            elif winner is False:
                pass
            elif winner is not False:
                s.addstr(0, 27, '[  {} WINS  ]'.format(winner))
                s.refresh()
                gs.end_game()
            else:
                pass

            '''
            TO DO:
                Restart pop-up for winner -> end_game() -> restart() if yes exit() if no

            '''

        while gs.gamestate['board_active']:
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
                if hk_showing:
                    hotkey_menu()
                    hk_showing = False
                else:
                    hk.clear()
                    hk.refresh()
                    hk_showing = True

            # Place pieces [Keys: E or Spacebar]
            elif c in (ord('e'), ord(' ')):
                place_piece()
                get_winner()

                # Reset Board [Key: Shift + R]
            elif c == ord('R'):
                b.clear()
                drawboard()

            # Exit [Key: Shift + Q]
            elif c == ord('Q'):
                b.clear()
                break

    hotkeys()


wrapper(main)

# testing purposes
print(gs.gamestate['board'])
print(gs.gamestate['board_active'])

'''

TO DO:
Internet co-op ? ❌

Splash Page: ?
    - Start ❌
    - Options [Online/Offline, Port, Color Theme] ❌
    - About ❌
    - Exit ❌

Status information:
    - won (p1 won/p2 won) ✔️
    - Reload ❌
    - Playing ❌

Tie in game logic:
    - set_piece() ✔️
    - win_check ✔️ -> end_game() ❌
    - reset() ❌


'''
