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
        # print(len(self.board), '=15?')
        self.color = colorMap[self.goal['color']]
        self.agent = getattr(copy.deepcopy(GAME), self.color)
        print(self.agent)
        # self.path = self.BFS(GAME)
        self.path_length = 0

    def heuristics_goal(self, GAME):
        goal_matrix = np.ones_like(game.board, dtype=np.uint8)*10
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
            moves = GAME.availableMovesEmptyBoard(self.agent)
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
    
    def heuristics_other(self, GAME):
        goal_matrix = np.ones_like(game.board, dtype=np.uint8)*10
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
            moves = GAME.availableMovesEmptyBoard(self.agent)
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

        # print("Depth: ", len(path[move_dir]))

        # self.path_length = weight(queue[-1])


if __name__ == "__main__":
    game = Ricochet()
    print(game.goal)
    solve = Solver(game)
    goal_matrix = solve.heuristics(game)
    print(goal_matrix)

    print(solve.agent)
    print(solve.goal)

    import matplotlib.pyplot as plt
    plt.imshow(goal_matrix, cmap='hot', interpolation='nearest')
    plt.show()

    # print(solve.path)
    # for solver.path do move
