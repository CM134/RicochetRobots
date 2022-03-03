# %%
from importlib.resources import path
import numpy as np
import random


class Ricochet:
    #TODO: Update board to not include agent positions, Agents only dicts
    def __init__(self, shape):
        self.shape = shape

        # create board
        self.board = self.initBoard()
        self.yellow = self.initAgent('Y')
        self.red = self.initAgent('R')
        self.blue = self.initAgent('B')
        self.green = self.initAgent('G')

    def initBoard(self):
        """Gernerate board

        Returns:
            numpy array: cells are either empty (0) or have walls in the edges of the cell (north 'N' east south west)
        """
        # TODO: Should be a fixed setup. Take a pic of the board and implement exactly that board.
        board = np.zeros((self.shape, self.shape), dtype=object)
        board[:, :] = '0'
        # Assign some random walls
        for _ in range(0, self.shape*3):
            idx_row, idx_col = self.randomSquare()
            if (board[idx_row, idx_col] != '0'):
                board[idx_row,
                      idx_col] += (random.choice(['S', 'W', 'N', 'E']))
            else:
                board[idx_row, idx_col] = random.choice(['S', 'W', 'N', 'E'])

        return board

    def initAgent(self, color):
        """initialise Agents with start position

        Args:
            color (Char): 'Y','G','R','B'

        Returns:
            dict: with name and position 
        """

        idx_row, idx_col = self.randomSquare()
        # two agents cannot be in the same square
        # if 'AG' in self.board[idx_row, idx_col]:
        #     self.initAgent(color)
        # else:
        #     self.board[idx_row, idx_col] += ':AG:'+color
        return {"name": color, "row": idx_row, "col": idx_col}

    def availableMoves(self, agent):
        #TODO: Work with 
        """computes all available endpositions for the moves as a dict. An Agent cannot collide with any wall or agent. 

        Args:
            agent (dict): yellow red green blue agent

        Returns:
            dict: move: position
        """

        # Move up
        for row in range(agent["row"], -1, -1):
            if (('S' in self.board[row, agent["col"]]) and (row != agent["row"])):
                u_row = row+1
                u_col = agent["col"]
                break
            elif ('N' in self.board[row, agent["col"]]):
                u_row = row
                u_col = agent["col"]
                break
            elif (('AG' in self.board[row, agent["col"]]) and (row != agent["row"])):
                u_row = row+1
                u_col = agent["col"]
                break
            elif (row == 0):
                u_row = row
                u_col = agent["col"]

        # Move down
        for row in range(agent["row"], self.shape):
            if (('N' in self.board[row, agent["col"]]) and (row != agent["row"])):
                d_row = row-1
                d_col = agent["col"]
                break
            elif ('S' in self.board[row, agent["col"]]):
                d_row = row
                d_col = agent["col"]
                break
            elif (('AG' in self.board[row, agent["col"]]) and (row != agent["row"])):
                d_row = row-1
                d_col = agent["col"]
                break
            elif (row == self.shape-1):
                d_row = row
                d_col = agent["col"]

        # Move left
        for col in range(agent["col"], -1, -1):
            if (('E' in self.board[agent["row"], col]) and (col != agent["col"])):
                l_row = agent["row"]
                l_col = col+1
                break
            elif ('W' in self.board[row, agent["col"]]):
                l_row = agent["row"]
                l_col = col
                break
            elif (('AG' in self.board[agent["row"], col]) and (col != agent["col"])):
                l_row = agent["row"]
                l_col = col+1
                break
            elif (col == 0):
                l_row = agent["row"]
                l_col = col

        # Move right
        for col in range(agent["col"], self.shape):
            if (('W' in self.board[agent["row"], col]) and (col != agent["col"])):
                r_row = agent["row"]
                r_col = col-1
                break
            elif ('E' in self.board[row, agent["col"]]):
                r_row = agent["row"]
                r_col = col
                break
            elif(('AG' in self.board[agent["row"], col]) and (col != agent["col"])):
                r_row = agent["row"]
                r_col = col-1
                break
            elif (col == self.shape-1):
                r_row = agent["row"]
                r_col = col

        return {'UP': (u_row, u_col),
                'DOWN': (d_row, d_col),
                'LEFT': (l_row, l_col),
                'RIGHT': (r_row, r_col)}

    def move(self, agent, move):
        """moves the agent in direction specified and updates the 

        Args:
            agent (_type_): color of the agent
            move (_type_): 'UP','DOWN','LEFT','RIGHT'
        """
        move_dict = self.availableMoves(agent)
        
        self.board[agent["row"], agent["col"]] = self.board[agent["row"], agent["col"]].replace((':AG:'+agent["name"]),'')
        agent["row"], agent["col"] = move_dict[move]
        self.board[agent["row"], agent["col"]]+=(':AG:'+agent["name"])

    # Helper Functions

    def randomSquare(self):
        idx_col = random.randint(0, self.shape-1)
        idx_row = random.randint(0, self.shape-1)
        return (idx_row, idx_col)



if __name__ == "__main__":
    
    b1 = Ricochet(10)
    print(b1.board)
    print(b1.yellow)
    print('\n')
    # b1.yellow["row"] = 0
    # b1.yellow["col"] = 1
    # b1.board[0, :] = "S"
    print(b1.availableMoves(b1.yellow))
    print("")
    b1.move(b1.yellow,'UP')
    print(b1.board)
# %%
