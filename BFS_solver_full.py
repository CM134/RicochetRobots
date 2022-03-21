from ricochet import Ricochet
import copy
from collections import deque
import time

class Solver:
    def __init__(self, GAME):
        self.colorMap = {'R': 'red', 'Y': 'yellow', 'G': 'green', 'B': 'blue'}
        self.goal = GAME.goal
        self.board = GAME.board
        self.Game = copy.deepcopy(GAME)
        self.color = self.colorMap[self.goal['color']]
        rest_colors = list(self.colorMap.values())
        rest_colors.remove(self.color)
        # Get all 4 robots, where robot0 is the goal robot
        self.agent0 = getattr(self.Game, self.color)
        for i in range(3):
            setattr(self, ("agent"+str(i+1)),
                    getattr(self.Game, rest_colors[i]))
        #Initialize BFS to perform search
        self.path = self.BFS()

    def getPoses(self):
        ag_ = []
        for i_ in range(4):
            ag_.append(getattr(self, ("agent"+str(i_))))
        ag_poses = [(ag_i["row"], ag_i["col"]) for ag_i in ag_]
        return tuple(ag_poses)

    def setPoses(self, pos_):
        for i_ in range(4):
            ag_i = getattr(self, "agent"+str(i_))
            ag_i["row"] = pos_[i_][0]
            ag_i["col"] = pos_[i_][1]

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

    def BFS(self):
        goal = ((self.goal["row"], self.goal["col"]))
        #Initialize the relative path
        visited = []
        queue = deque()
        path = {}

        root_pos = self.getPoses()
        queue.append(root_pos)
        visited.append(root_pos)
        path[root_pos] = (None, 0, (None, None)) # (Parent, Depth (Color, Direction))
        depth = 0
        depth_old = depth
        time0 = time.time()
        while ((time.time()-time0) < 60) and (len(queue) != 0):
            pos = queue.popleft()
            for i in range(4):  # Robot Level
                self.setPoses(pos)  # Resets all poses to queue start positions
                ag = getattr(self, "agent"+str(i))
                ag["row"] = pos[i][0]
                ag["col"] = pos[i][1]
                moves = self.Game.availableMoves(ag)
                for dir in ['UP', 'DOWN', 'LEFT', 'RIGHT']:
                    move_dir = moves[dir]
                    new_pos = [p_ for p_ in pos]
                    new_pos[i] = move_dir
                    new_pos = tuple(new_pos)
                    if new_pos not in visited:
                        if (move_dir == goal) and i == 0:
                            print("FOUND GOAL!!!!")
                            path[new_pos] = (pos, path[pos][1]+1, (self.colorMap[ag['name']], dir))
                            return self.backtracePath(path, new_pos)
                        queue.append(new_pos)
                        visited.append(new_pos)
                        path[new_pos] = (pos, path[pos][1]+1, (self.colorMap[ag['name']], dir))
                        depth = path[new_pos][1]
                        if depth > depth_old:
                            print('depth:', depth)
                            print('queue length:', len(queue))
                            print('visited length:', len(visited))
                            depth_old = depth
        return None #Return None as path if unable to find within constrains

if __name__ == "__main__":

    game = Ricochet()

    print(game.goal)
    solve = Solver(game)
    print(solve.agent0)
    print(solve.goal)
    print(solve.path)
