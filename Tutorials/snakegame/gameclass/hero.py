import curses
import os
import time

class Hero():
    
    def __init__(self,head,screen,direction):
        self.head = head
        self.screen = screen
        self.direction = direction
    	self.screen.border()
    	self.screen.keypad(1)
    	self.screen.nodelay(1)
        
    def update(self):
        if self.direction == 3:
            self.head[0] -=1
       
        elif self.direction == 2:
            self.head[0] += 1
      
        elif self.direction == 1:
            self.head[1] -= 1
  
        elif self.direction == 0:
            self.head[1] += 1
    
        self.screen.refresh()
        time.sleep(0.1)
    
    def display(self):
       
        self.screen.addch(self.head[0],self.head[1],'x')
     
            
    def process_input(self):
        userinput = self.screen.getch()
        if userinput == curses.KEY_UP:
            self.direction = 3
        elif userinput == curses.KEY_DOWN:
            self.direction = 2
        elif userinput == curses.KEY_LEFT:
            self.direction = 1
        elif userinput == curses.KEY_RIGHT:
            self.direction = 0
        else:    
            self.direction = 4
            
    def collide(self):
        """This function is used to detect a collision"""
        if self.direction == 3 and self.screen.inch(self.head[0]-1,self.head[1]) !=ord(' '):
            return True
        elif self.direction == 2 and self.screen.inch(self.head[0]+1,self.head[1]) !=ord(' '):
            return True
        elif self.direction == 1 and self.screen.inch(self.head[0],self.head[1]-1) !=ord(' '):
            return True
        elif self.direction == 0 and self.screen.inch(self.head[0],self.head[1]+1) !=ord(' '):
            return True    
        else:
            return False  
        
    def hero_exit(self):
        os.system('cls' if os.name == 'nt' else 'reset')
        exit()
        



    
    

            
