# %%

import numpy as np
import random

from board_layouts.board_1 import board, goal_list, SIZE

class Ricochet:
    def __init__(self):
        self.shape = SIZE

        # create board
        self.board = board
        
        self.agent_list = [] 
        self.yellow = self.initAgent('Y')
        self.agent_list.append(self.yellow)
        
        self.red = self.initAgent('R')
        self.agent_list.append(self.red)
        
        self.blue = self.initAgent('B')
        self.agent_list.append(self.blue)
        
        self.green = self.initAgent('G')
        self.agent_list.append(self.green)
        
        self.goal_list = goal_list
        self.setGoal()
        

    def initBoard(self):
        """Generate board (not used at the moment. In the future we can make different boards and choose the right setup from here )

        Returns:
            numpy array: cells are either empty (0) or have walls in the edges of the cell (north 'N' east south west)
        """
        # board = np.zeros((self.shape, self.shape), dtype=object)
        # board[:, :] = '0'
        # # Assign some random walls
        # for _ in range(0, self.shape*3):
        #     idx_row, idx_col = self.randomSquare()
        #     if (board[idx_row, idx_col] != '0'):
        #         board[idx_row,
        #               idx_col] += (random.choice(['S', 'W', 'N', 'E']))
        #     else:
        #         board[idx_row, idx_col] = random.choice(['S', 'W', 'N', 'E'])

        # return board
        pass

    def initAgent(self, color):
        """initialise Agents with start position

        Args:
            color (Char): 'Y','G','R','B'

        Returns:
            dict: with name and position 
        """

        idx_row, idx_col = self.randomSquare()
        
        # check if inside the center square:
        if idx_row == 7 and idx_col == 7:
            self.initAgent(color)
        elif idx_row == 7 and idx_col == 8:
            self.initAgent(color)
        elif idx_row == 8 and idx_col == 7:
            self.initAgent(color)
        elif idx_row == 8 and idx_col == 8:
            self.initAgent(color)
        
        # two agents cannot be in the same square
        for agent in self.agent_list:
            if len(self.agent_list)>0:
                if ((agent['row'] == idx_row) and (agent['col']==idx_col)):
                    self.initAgent(color)
            
        return {"name": color, "row": idx_row, "col": idx_col}
        
    def setGoal(self):
        self.goal = random.choice(goal_list)
        
    def availableMoves(self, agent):
        """computes all available endpositions for the moves as a dict. An Agent cannot collide with any wall or agent. 

        Args:
            agent (dict): yellow red green blue agent

        Returns:
            dict: move: position
        """

        # Move up
        agent_hit = False
        for row in range(agent["row"], -1, -1):
            for other in self.agent_list:
                if other['name'] == agent['name']:
                    continue
                elif ((other['col'] == agent['col'] and other['row']== row)):
                    u_row = row+1
                    u_col = agent["col"]
                    agent_hit = True
                    break
            if agent_hit:  # didn't know how to break a loop twice
                break
            if (('S' in self.board[row, agent["col"]]) and (row != agent["row"])):
                u_row = row+1
                u_col = agent["col"]
                break
            elif ('N' in self.board[row, agent["col"]]):
                u_row = row
                u_col = agent["col"]
                break
            elif (row == 0):
                u_row = row
                u_col = agent["col"]
                break

        # Move down
        agent_hit = False
        for row in range(agent["row"], self.shape):
            
            for other in self.agent_list:
                if other['name'] == agent['name']:
                    continue
                elif ((other['col'] == agent['col'] and other['row']== row)):
                    d_row = row-1
                    d_col = agent["col"]
                    agent_hit = True
                    break
            if agent_hit:
                break
            if (('N' in self.board[row, agent["col"]]) and (row != agent["row"])):
                d_row = row-1
                d_col = agent["col"]
                break
            elif ('S' in self.board[row, agent["col"]]):
                d_row = row
                d_col = agent["col"]
                break
            elif (row == self.shape-1):
                d_row = row
                d_col = agent["col"]
                break

        # Move left
        agent_hit = False
        for col in range(agent["col"], -1, -1):
            
            for other in self.agent_list:
                if other['name'] == agent['name']:
                    continue
                elif ((other['row'] == agent['row'] and other['col']== col)):
                    l_row = agent["row"]
                    l_col = col+1
                    agent_hit = True
                    break
            if agent_hit:
                break
            if ('E' in self.board[agent["row"], col] and (col != agent["col"])):
                l_row = agent["row"]
                l_col = col+1
                break
            elif ('W' in self.board[agent["row"], col]):
                l_row = agent["row"]
                l_col = col
                break
            elif (col == 0):
                l_row = agent["row"]
                l_col = col
                break

        # Move right
        agent_hit = False
        for col in range(agent["col"], self.shape):
            
            for other in self.agent_list:
                if other['name'] == agent['name']:
                    continue
                elif ((other['row'] == agent['row'] and other['col']== col)):
                    r_row = agent["row"]
                    r_col = col-1
                    agent_hit = True
                    break
            if agent_hit:      
                break
            if ('W' in self.board[agent["row"], col] and (col != agent["col"])):
                r_row = agent["row"]
                r_col = col-1
                break
            elif ('E' in self.board[agent["row"], col]):
                r_row = agent["row"]
                r_col = col
                break 
            elif (col == self.shape-1):
                r_row = agent["row"]
                r_col = col
                break

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


#%%
if __name__ == "__main__":
    
    b1 = Ricochet()
    print(b1.board)
    print(b1.goal)
    print(b1.agent_list)
    print(b1.yellow)
    print('\n')
    # # b1.yellow["row"] = 0
    # # b1.yellow["col"] = 1
    # # b1.board[0, :] = "S"
    print(b1.availableMoves(b1.yellow))
    print("")
    b1.move(b1.yellow,'UP')
    print(b1.yellow)
    # print(b1.board)
# %%



# %%
