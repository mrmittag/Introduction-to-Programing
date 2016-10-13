import curses
import time
import random

screen = curses.initscr()
#screen.nodelay(0)
head = [1,1]
body = [head[:]]*5

screen.border()

direction = 0 #0 =right, 1 =down 2 = left 3 =up
gameOver= False


def game():

	while not gameOver:
		screen.addch(head[0], head[1],'x')

		if direction ==0:
			head[1] += 1
		elif direction ==2:
			head[1] -= 1
		elif direction == 1:
			head[0] += 1
		elif direction == 3:
			head[0] -= 1
		
		if screen.inch(head[0],head[1]) != ord(' '):
			gameover =True
		screen.refresh()
		time.sleep(0.1)
game()
curses.edwin()

