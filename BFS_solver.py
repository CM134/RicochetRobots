# Pseudo code for implementation of the AI.
from ricochet import Ricochet
from visualizer import Visualizer
import copy
import pdb

class Solver:
    def __init__(self, GAME):
        colorMap = {'R':'red', 'Y':'yellow', 'G':'green', 'B':'blue'}
        self.goal = GAME.goal
        self.board = GAME.board
        self.color = colorMap[self.goal['color']]
        self.agent = getattr(copy.deepcopy(GAME), self.color)
        print(self.agent)
        self.path = self.BFS(GAME)

    def BFS(self, GAME):
        goal = ((self.goal["row"], self.goal["col"]))
        visited = []
        queue = []
        path = {}

        root_pos = (self.agent["row"], self.agent["col"])
        queue.append(root_pos)
        visited.append(root_pos)
        path[root_pos] = []

        for i in range(100):
            print(i)
            pos = queue.pop(0)
            self.agent['row'] = pos[0]
            self.agent['col'] = pos[1]
            print(self.agent)
            moves = GAME.availableMoves(self.agent)
            for dir in ['UP', 'DOWN', 'LEFT', 'RIGHT']:
                #pdb.set_trace()
                move_dir = moves[dir]
                #print(move_dir)
                if move_dir not in visited:
                    if move_dir == goal:
                        print("FOUND GOAL!!!!")
                        path[move_dir] = path[pos].copy()
                        path[move_dir].append(dir)
                        return path[move_dir]
                    queue.append(move_dir)
                    visited.append(move_dir)
                    path[move_dir] = path[pos].copy()
                    path[move_dir].append(dir)
    
game = Ricochet()
print(game.goal)
solve = Solver(game)

print(solve.agent)
print(solve.goal)
print(solve.path)
#for solver.path do move