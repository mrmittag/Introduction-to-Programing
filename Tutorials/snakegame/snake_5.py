import curses
import time
import os

screen = curses.initscr()	# Create screen object 
head=[1,1]					# This is a list that holds the y and x coordinates of the snake

def initialize():
	"""This function sets the attributes and appearence of our screen"""
	screen.border()
	screen.keypad(1)
	screen.nodelay(1)


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
    """This function updates the state of the game. It advances the game one step.""" 
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
    
def start():
	"""This function is used to aske the user if they would like to start could also be used for any instructions"""
	screen.nodelay(0)
	screen.addstr("press 's' to start")
	choice = screen.getch()
	if choice == ord('s'):
		screen.clear()
		return False
	else:
		return True
	
def display():
    """This function draws all of the stuff in the game"""
    screen.addch(head[0],head[1],'x')

def endgame():
	"""This screen asks the user if they would like to play again if not it exits the program"""
	screen.nodelay(0)
	screen.addstr("Would you like to play again? press y or n")
	choice = screen.getch()
	if choice == ord('y'):
		screen.clear()
		game()
	else:
		os.system('cls' if os.name == 'nt' else 'reset') # this line resets the terminal window back to normal


def game():
	"""This is our basic game loop wraped inside a function """
	game_over = start() # we set the variable game_over to the results of calling the start function
	initialize() 
	direction =0
	while game_over == False:
		direction = processInput(direction)
		update(direction)
		display()
		game_over = collison(direction)	
	endgame()

game()
