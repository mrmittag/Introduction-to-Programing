import curses
import time
import random

screen = curses.initscr()
screen.nodelay(1)
head = [1,1]
body = [head[:]]*5
screen.keypad(1)
screen.border()
gameOver= False

def game():
    direction = 0
    while not gameOver:
        
        screen.addch(head[0], head[1],'x')
        direction = keyupdate(direction)
        
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
    

        
def keyupdate(direction):
    userinput = screen.getch()
    if userinput == curses.KEY_UP:
        direction = 3
    elif userinput == curses.KEY_DOWN:
        direction = 1
    elif userinput == curses.KEY_LEFT:
        direction = 2
    elif userinput == curses.KEY_RIGHT:
        direction = 0
    return direction

   
    
game()
curses.edwin()

