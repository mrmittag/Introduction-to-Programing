import curses
import time

screen = curses.initscr()
screen.border()
screen.nodelay(1)
screen.keypad(1)

direction =0 
game_over =False  
head=[1,1]

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
    """This function updates the state of the game. It advances the game one step. Performs AI and Physics""" 
    if direction == 3:
        head[0] -=1
    elif direction == 2:
        head[0] += 1
    elif direction == 1:
        head[1] -= 1
    elif direction == 0:
        head[1] += 1
        
    screen.refresh()
    time.sleep(0.1)
    
def collison(direction):
    """This function is used to detect a collision"""
    if direction == 3 and screen.inch(head[0]-1,head[1]) !=ord(' '):
        return True
    elif direction == 2 and screen.inch(head[0]+1,head[1]) !=ord(' '):
        return True
    elif direction == 1 and screen.inch(head[0],head[1]-1) !=ord(' '):
        return True
    elif direction == 0 and screen.inch(head[0],head[1]+1) !=ord(' '):
        return True    
    else:
        return False
    

def display():
    """This function draws all of the stuff in the game"""
    screen.addch(head[0],head[1],'x')

while game_over == False:
    direction = processInput(direction)
    update(direction)
    display()
    game_over = collison(direction)
    
curses.endwin()
    

    

