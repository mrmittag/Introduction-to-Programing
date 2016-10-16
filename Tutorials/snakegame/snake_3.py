import curses
import time

screen = curses.initscr()
screen.border()
screen.nodelay(1)
head=[1,1]
screen.keypad(1)
direction =0 
    
def processInput(direction):
    """This function processes any user input"""
    userinput = screen.getch()
    if userinput == curses.KEY_UP:
        direction = 3
    elif userinput == curses.KEY_DOWN:
        direction = 2
    elif userinput == curses.KEY_LEFT:
        direction = 1
    elif userinput == curses.KEY_RIGHT:
        direction = 0
    return direction
    
    
def update(direction):
    """This function updates the state of the game. It advances the game one step.Performs AI and Physics""" 
    if direction == 3:
        head[0] -=1
    elif direction == 2:
        head[0] += 1
    elif direction == 1:
        head[1] -= 1
    elif direction == 0:
        head[1] += 1
        
    if screen.inch(head[0],head[1]) != ord(' '):
        gameover =True
    screen.refresh()
    time.sleep(0.1)
    

def display():
    """This function draws all of the stuff in the game"""
    screen.addch(head[0],head[1],'x')
      
while True:
    direction = processInput(direction)
    update(direction)
    display()
    
curses.edwin()
    

