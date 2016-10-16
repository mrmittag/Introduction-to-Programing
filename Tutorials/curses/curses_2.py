import curses

screen = curses.initscr()

screen.addstr(4,9,'HelloWord')
screen.refresh()
screen.getch()
curses.endwin()
