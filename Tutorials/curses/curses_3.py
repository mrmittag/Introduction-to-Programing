import curses
import time

screen = curses.initscr()
dims = screen.getmaxyx()

for x in range(100):
	screen.clear()
	screen.addstr(0,x,'HelloWorld')
	screen.refresh()
	time.sleep(0.2)
#screen.getch()
screen.edwin()

