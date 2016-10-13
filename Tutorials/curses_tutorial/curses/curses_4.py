import curses
import time

screen = curses.initscr()
x,y = 0,0 
userinput = ord('p')

while userinput != ord('q'):
	screen.clear()
	screen.addstr(y,x,'HelloWorld')
	screen.refresh()
	userinput = screen.getch()

curses.endwin()
