# Pseudo code for implementation of the AI.
from tkinter.tix import CELL
from types import CellType
from ricochet import Ricochet
from visualizer import Visualizer
import copy
import pdb
import numpy as np


class Solver:
    def __init__(self, GAME):
        colorMap = {'R': 'red', 'Y': 'yellow', 'G': 'green', 'B': 'blue'}
        self.goal = GAME.goal
        self.board = GAME.board
        self.game = GAME
        self.color = colorMap[self.goal['color']]
        self.agent = getattr(copy.deepcopy(GAME), self.color)
        self.goal_matrix = self.heuristics_goal()
        self.other_matrix = self.heuristics_other()

    def heuristics_goal(self):
        """generate heuristics for goal agent. Heuristics indicate number 
        of moves to goa.
        
        Standard BFS search to compute the weighted matrix. 

        Returns:
            goal_matrix: matrix of weights
        """

        goal_matrix = np.ones_like(self.board, dtype=np.uint8)*6
        goal = ((self.goal["row"], self.goal["col"]))
        visited = []
        queue = []
        path = {}

        root_pos = goal
        goal_matrix[root_pos] = 0

        queue.append(root_pos)
        visited.append(root_pos)
        path[root_pos] = []
        weight = 0
        while len(queue) is not 0:
            pos = queue.pop(0)
            # print(pos)
            self.agent['row'] = pos[0]
            self.agent['col'] = pos[1]
            moves = self.game.availableMovesEmptyBoard(self.agent)
            for dir in ['UP', 'DOWN', 'LEFT', 'RIGHT']:
                move_dir = moves[dir]
                # search each cell on path
                cell_list = []
                if dir == 'UP':
                    for row in range(self.agent["row"], move_dir[0], -1):
                        cell = (row, self.agent["col"])
                        cell_list.append(cell)
                if dir == 'DOWN':
                    for row in range(self.agent["row"], move_dir[0]):
                        cell = (row, self.agent["col"])
                        cell_list.append(cell)
                if dir == 'RIGHT':
                    for col in range(self.agent["col"], move_dir[1]):
                        cell = (self.agent["row"], col)
                        cell_list.append(cell)
                if dir == 'LEFT':
                    for col in range(self.agent["col"], move_dir[1], -1):
                        cell = (self.agent["row"], col)
                        cell_list.append(cell)

                for cell in cell_list:
                    if cell not in visited:
                        goal_matrix[cell] = goal_matrix[pos]+1
                        queue.append(cell)
                        visited.append(cell)

                weight += 1

        return goal_matrix

    def heuristics_other(self):
        """computes the matrix of weights of the non goal agents. 
        The squares with the lowest cost is the one which the goal 
        agent can bounce of and go directly into the goal
        
        Standard BFS search with initial computation of preferable squares

        Returns:
            other_matrix: matrix of weights
        """
        inter_matrix = np.ones_like(self.board, dtype=np.uint8)*6
        goal = ((self.goal["row"], self.goal["col"]))
        visited = []
        queue = []

        root_pos = goal
        inter_matrix[root_pos] = 0
        pos = root_pos

        queue.append(root_pos)
        visited.append(root_pos)
        weight = 0

        self.agent['row'] = root_pos[0]
        self.agent['col'] = root_pos[1]
        moves = self.game.availableMovesEmptyBoard(self.agent)
        for dir in ['UP', 'DOWN', 'LEFT', 'RIGHT']:
            move_dir = moves[dir]
            # search each cell on path
            cell_list = []
            if dir == 'UP':
                for row in range(self.agent["row"], move_dir[0], -1):
                    if self.agent["col"] != 0:  # otherwise out of range
                        cell = (row, self.agent["col"]-1)
                        cell_list.append(cell)
                    if self.agent["col"] != len(self.board)-1:
                        cell = (row, self.agent["col"]+1)
                        cell_list.append(cell)
            if dir == 'DOWN':
                for row in range(self.agent["row"], move_dir[0]):
                    if self.agent["col"] != 0:
                        cell = (row, self.agent["col"]-1)
                        cell_list.append(cell)
                    if self.agent["col"] != len(self.board)-1:
                        cell = (row, self.agent["col"]+1)
                        cell_list.append(cell)
            if dir == 'RIGHT':
                for col in range(self.agent["col"], move_dir[1]):
                    if self.agent["row"] != 0:
                        cell = (self.agent["row"], col-1)
                        cell_list.append(cell)
                    if self.agent["row"] != len(self.board)-1:
                        cell = (self.agent["row"], col-1)
                        cell_list.append(cell)
            if dir == 'LEFT':
                for col in range(self.agent["col"], move_dir[1]):
                    if self.agent["row"] != 0:
                        cell = (self.agent["row"], col-1)
                        cell_list.append(cell)
                    if self.agent["row"] != len(self.board)-1:
                        cell = (self.agent["row"], col-1)
                        cell_list.append(cell)

            for cell in cell_list:
                if cell not in visited:
                    inter_matrix[cell] = weight
                    queue.append(cell)
                    visited.append(cell)

        # GOAL SEARCH

        while len(queue) is not 0:
            pos = queue.pop(0)
            # print(pos)
            self.agent['row'] = pos[0]
            self.agent['col'] = pos[1]
            moves = self.game.availableMovesEmptyBoard(self.agent)
            for dir in ['UP', 'DOWN', 'LEFT', 'RIGHT']:
                move_dir = moves[dir]
                # search each cell on path
                cell_list = []
                if dir == 'UP':
                    for row in range(self.agent["row"], move_dir[0], -1):
                        cell = (row, self.agent["col"])
                        cell_list.append(cell)
                if dir == 'DOWN':
                    for row in range(self.agent["row"], move_dir[0]):
                        cell = (row, self.agent["col"])
                        cell_list.append(cell)
                if dir == 'RIGHT':
                    for col in range(self.agent["col"], move_dir[1]):
                        cell = (self.agent["row"], col)
                        cell_list.append(cell)
                if dir == 'LEFT':
                    for col in range(self.agent["col"], move_dir[1], -1):
                        cell = (self.agent["row"], col)
                        cell_list.append(cell)

                for cell in cell_list:
                    if cell not in visited:
                        inter_matrix[cell] = inter_matrix[pos]+1
                        queue.append(cell)
                        visited.append(cell)

        return inter_matrix + self.goal_matrix


if __name__ == "__main__":
    game = Ricochet()
    print(game.goal)

    solve = Solver(game)
    print(solve.agent)
    print(solve.goal)

    # other_matrix = solve.heuristics_other()
    other_matrix = solve.other_matrix
    print(other_matrix)

    import matplotlib.pyplot as plt
    plt.imshow(other_matrix, cmap='hot', interpolation='nearest')
    plt.show()

    # goal_matrix = solve.heuristics_goal()
    goal_matrix = solve.goal_matrix
    print(goal_matrix)

    import matplotlib.pyplot as plt
    plt.imshow(goal_matrix, cmap='hot', interpolation='nearest')
    plt.show()

    # print(solve.path)
    # for solver.path do move
