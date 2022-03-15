# Pseudo code for implementation of the AI.
from ricochet import Ricochet
from visualizer import Visualizer
import copy
import pdb

class Solver:
    def __init__(self, GAME):
        self.colorMap = {'R':'red', 'Y':'yellow', 'G':'green', 'B':'blue'}
        self.goal = GAME.goal
        self.board = GAME.board
        self.Game = copy.deepcopy(GAME)
        self.color = self.colorMap[self.goal['color']]
        rest_colors = list(self.colorMap.values())
        rest_colors.remove(self.color)
        #Add other robots
        self.agent0 = getattr(self.Game, self.color)
        for i in range(3):
            setattr(self,("agent"+str(i+1)), getattr(self.Game, rest_colors[i]))
        self.path = self.BFS()

    def getPoses(self):
        ag_ = []
        for i_ in range(4):
            ag_.append(getattr(self,("agent"+str(i_))))
        ag_poses = [(ag_i["row"], ag_i["col"]) for ag_i in ag_]
        return tuple(ag_poses)

    def setPoses(self,pos_):
        for i_ in range(4):
            ag_i = getattr(self, "agent"+str(i_))
            ag_i["row"] = pos_[i_][0]
            ag_i["col"] = pos_[i_][1]

    def BFS(self):
        goal = ((self.goal["row"], self.goal["col"]))
        visited = []
        queue = []
        path = {}

        root_pos = self.getPoses()
        queue.append(root_pos)
        visited.append(root_pos)
        path[root_pos] = []
        depth = 0
        print(root_pos)
        while (depth < 8) and len(path)<30000:
            pos = queue.pop(0)
            for i in range(4): # Robot Level
                self.setPoses(pos) #Resets all poses to queue start positions
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
                        if (move_dir == goal) and i==0:
                            print("FOUND GOAL!!!!")
                            path[new_pos] = path[pos].copy()
                            path[new_pos].append((self.colorMap[ag['name']], dir))
                            return path[new_pos]
                        queue.append(new_pos)
                        visited.append(new_pos)
                        path[new_pos] = path[pos].copy()
                        path[new_pos].append((self.colorMap[ag['name']], dir))
                        depth = len(path[new_pos])
 
       #pdb.set_trace()
       
if __name__ == "__main__":

    game = Ricochet()


    print(game.goal)
    solve = Solver(game)
    print(solve.agent0)
    print(solve.goal)
    print(solve.path)
    #for solver.path do move