import curses

screen = curses.initscr()

screen.addstr(4,9,'HelloeWord')
screen.refresh()
screen.getch()
curses.endwin()
