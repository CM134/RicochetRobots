# Pseudo code for implementation of the AI.
from ricochet import Ricochet
import copy
import time
from collections import deque

class Solver:
    def __init__(self, GAME):
        colorMap = {'R':'red', 'Y':'yellow', 'G':'green', 'B':'blue'}
        self.goal = GAME.goal
        self.board = GAME.board
        self.color = colorMap[self.goal['color']]
        self.agent = getattr(copy.deepcopy(GAME), self.color)
        print(self.agent)
        self.path = self.BFS(GAME)
        self.path_length = 0

    #Moves up the graph between each child-parent pair
    def backtracePath(self, pth, goalPos):
        parent = 1
        goalPath = []
        parent_ = goalPos
        #Backtrace path until depth 1
        depth_ = 100
        while depth_ > 1:
            parent_, depth_, colorDir_ = pth[parent_]
            goalPath.append(colorDir_)
        goalPath.reverse()
        return goalPath

    def BFS(self, GAME):
        goal = ((self.goal["row"], self.goal["col"]))
        visited = []
        queue = deque()
        path = {}

        root_pos = (self.agent["row"], self.agent["col"])
        queue.append(root_pos)
        visited.append(root_pos)
        path[root_pos] = (None, 0, (None, None)) # (Parent, Depth (Color, Direction))

        time0 = time.time()
        while ((time.time()-time0) < 60) and (len(queue) != 0):
            pos = queue.popleft()
            self.agent['row'] = pos[0]
            self.agent['col'] = pos[1]
            print(self.agent)
            moves = GAME.availableMoves(self.agent)
            for dir in ['UP', 'DOWN', 'LEFT', 'RIGHT']:
                move_dir = moves[dir]
                if move_dir not in visited:
                    if move_dir == goal:
                        print("FOUND GOAL!!!!")
                        path[move_dir] = (pos, path[pos][1]+1, (self.color, dir))
                        return self.backtracePath(path, move_dir)
                    queue.append(move_dir)
                    visited.append(move_dir)
                    path[move_dir] = (pos, path[pos][1]+1, (self.color, dir))
                    print("Depth: ", path[move_dir][1])
                    self.path_length = len(path[move_dir])
        return None #Return path as None if unable to find within constrains
                    

if __name__ == "__main__":
    game = Ricochet()
    print(game.goal)
    solve = Solver(game)

    print(solve.agent)
    print(solve.goal)
    print(solve.path)
    #for solver.path do move