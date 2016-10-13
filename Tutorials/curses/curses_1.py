#https://docs.python.org/2/library/curses.html

import curses

screen = curses.initscr()
screen.addstr(0,0, 'HelloWorld') #screen.addstr(0,0, 'HelloWorld',curses.A_BOLD)
screen.refresh()
screen.getch()
curses.endwin()	#De-initialize the library, and return terminal to normal status.

