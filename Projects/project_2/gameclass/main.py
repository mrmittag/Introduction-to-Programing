import curses            
import time
import os
# import the hero,board and other classes need to create the game.
from hero import *          
from board import *

screen = curses.initscr()
direction = 0
hero = Hero([5,5],screen,direction)
board = Board(screen)
curses.curs_set(0)

def init():
    direction =4
    hero.head=[5,5]

def update():
    hero.update()
    board.update()
    collide()
      
def collide():
    test = hero.collide()
    if test == True:
        return True
    elif test == False:
       return False
          
def display():
    board.display()
    hero.display()
       
def process_input():
   hero.process_input()
 
if __name__=="__main__":
    init()
    
    try:
        while True:
            process_input()
            update()
            display()
                      
    except:
        os.system('cls' if os.name == 'nt' else 'reset')
