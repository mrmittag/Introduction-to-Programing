class Board():
    """Class for drawing game board"""
    def __init__(self,screen):
        self.screen=screen
    
    def update(self):
        pass
    
    def display(self):
        self.screen.addstr(3,3,"This is the board")
       

    
