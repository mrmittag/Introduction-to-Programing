import curses            
import time
import os

from hero import *          # import the hero,board and other classes need to create the game.
from board import *

screen = curses.initscr()
direction = 0
x = Hero([5,5],screen,direction)
board =Board(screen)


def init():
    direction =4
    x.head=[5,5]

def update():
    x.update()
    board.update()
    collide()
      
def collide():
    test = x.collide()
    if test == True:
        c = "hit"
    elif test == False:
        c = "no hit"
    screen.addstr(6,6,c)
        
def display():
    board.display()
    x.display()
       
def process_input():
   x.process_input()
 
if __name__=="__main__":
    init()
    
    try:
        while True:
            process_input()
            update()
            display()
            
            
    except:
        os.system('cls' if os.name == 'nt' else 'reset')
