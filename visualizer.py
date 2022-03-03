#Pseudo code

from ricochet import Ricochet
from constants import *
import numpy as np

class Visualizer:
    
    PADDING = 10
    OUTLINE = 2
    radius = SQUARE_SIZE//2 - PADDING
    def __init__(self,game):
        self.game = game
        print(self.game)
        #print(self.game[0,:])
        #print(self.game[:,0])
        

    def draw_board(self,win):
        radius = SQUARE_SIZE//2 - self.PADDING
        win.fill(WHITE)
        for x in range(0, WIDTH, SQUARE_SIZE):
            for y in range(0, HEIGHT, SQUARE_SIZE):
                rect = pygame.Rect(x, y, SQUARE_SIZE, SQUARE_SIZE)
                pygame.draw.rect(win, BLACK, rect, 1)

        for col in range(COLS):
            for row in range(ROWS):
                center = np.array([(SQUARE_SIZE//2)+SQUARE_SIZE*col,(SQUARE_SIZE//2)+SQUARE_SIZE*row])
                #print('row,col: ',row,col)
                #print('self.game[row,col]:' , self.game[row,col])
                if 'N' in self.game[row,col]:
                    #print(center[0]-SQUARE_SIZE//2)            
                    pygame.draw.line(win, RED, (center[0]-SQUARE_SIZE//2,center[1]-SQUARE_SIZE//2),(center[0]+SQUARE_SIZE//2,center[1]-SQUARE_SIZE//2), width=5)
                   
                
                if 'S' in self.game[row,col]:
                    pygame.draw.line(win, RED, (center[0]-SQUARE_SIZE//2,center[1]+SQUARE_SIZE//2),(center[0]+SQUARE_SIZE//2,center[1]+SQUARE_SIZE//2), width=5)

                if 'E' in self.game[row,col]:
                    pygame.draw.line(win, RED, (center[0]+SQUARE_SIZE//2,center[1]-SQUARE_SIZE//2),(center[0]+SQUARE_SIZE//2,center[1]+SQUARE_SIZE//2), width=5)

                if 'W' in self.game[row,col]:
                    pygame.draw.line(win, RED, (center[0]-SQUARE_SIZE//2,center[1]+SQUARE_SIZE//2),(center[0]-SQUARE_SIZE//2,center[1]-SQUARE_SIZE//2), width=5)
                    



    #def draw_board(self):
        #for col and rows:
        #    if nswe:
        #        draw_line()
        #for agent:
        #    draw agent in color at col row
        
        #draw_goal()
   #
    #def show_moves:
        #game.availableMoves(agent)
        #draw_moves()
    # in main show make & update game instance.