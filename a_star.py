from Heuristics import Heuristics
from ricochet import Ricochet
import copy

class Node():
    """A node class for A* Pathfinding"""

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0
        
        self.agent_nr = 0   # 0 for goal agent, 1 for other agent
        self.move = ''      # last move executed
        self.color = ''     # last moves agent color
        
    def __eq__(self, other):
        return self.position == other.position


class AStar:
    def __init__(self, game):
        self.colorMap = {'R':'red', 'Y':'yellow', 'G':'green', 'B':'blue'}
        self.goal = game.goal
        self.board = game.board
        self.game = copy.deepcopy(game)
        self.color = self.colorMap[self.goal['color']]
        rest_colors = list(self.colorMap.values())
        rest_colors.remove(self.color)
        #Add other robots
        self.agent0 = getattr(self.game, self.color)
        for i in range(3):
            setattr(self,("agent"+str(i+1)), getattr(self.game, rest_colors[i]))
        H = Heuristics(game)    
        self.h_goal = H.goal_matrix
        self.h_other = H.other_matrix
        
        self.path = self.astar()
        
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
            
    def astar(self):
        """Returns a list of tuples as a path from the given start to the given end in the given maze"""
        deepest_depth = 0
        # Create start
        root_pos = self.getPoses()
        goal = ((self.goal["row"], self.goal["col"]))
        start_node = Node(None, root_pos)
        start_node.g = start_node.h = start_node.f = 0

        # Initialize both open and closed list
        open_list = []
        closed_list = []

        # Add the start node
        open_list.append(start_node)

        # Loop until you find the end
        while len(open_list) > 0:

            # Get the current node with lowest f
            current_node = open_list[0]
            current_index = 0
            for index, item in enumerate(open_list):
                if item.f < current_node.f:
                    current_node = item
                    current_index = index

            # Pop current off open list, add to closed list
            open_list.pop(current_index)
            closed_list.append(current_node)

            # Found the goal
            if current_node.position[0] == goal:
                path = []
                current = current_node
                while current is not None:
                    path.append((current.color,current.move))
                    current = current.parent
                path = path[::-1] # Return reversed path
                return path [1:] # fist argument of path is '',''. We want to skip that.

            # Generate children:
            # iterate through robots and each possible robot move
            children = []
            pos = current_node.position
            for i in range(4): # Adjacent squares
                self.setPoses(pos) # Resets all poses to queue start positions
                ag = getattr(self, "agent"+str(i))
                ag["row"] = pos[i][0]
                ag["col"] = pos[i][1]
                moves = self.game.availableMoves(ag)
                for dir in ['UP', 'DOWN', 'LEFT', 'RIGHT']:
                    moved_pos = moves[dir]
                    new_pos = [p_ for p_ in pos]    # old pos
                    new_pos[i] = moved_pos          # update with move  
                    new_pos = tuple(new_pos)        # cast tuple

                    # Create new node and append
                    new_node = Node(current_node, new_pos)
                    new_node.agent_nr = i
                    new_node.move = dir
                    new_node.color = self.colorMap[ag['name']]
                    
                    if new_node not in closed_list:
                        try:
                            idx = open_list.index(new_node) # fails if node not in list
                            new_node.g = current_node.g + 1
                            open_node = open_list[idx]
                            if new_node.g < open_node.g:
                                children.append(new_node)
                                open_list.remove(open_node)
                        except:
                            children.append(new_node)

            # Loop through children
            for child in children:


                # Create the f, g, and h values
                
                child.g = current_node.g + 1   # comment this and you get greedy search
                if child.agent_nr == 0:
                    child.h = self.h_goal[child.position[0]]
                else:
                    child.h = self.h_other[child.position[child.agent_nr]]
                child.f = child.g + child.h


                # Add the child to the open list
                open_list.append(child)
            
                if deepest_depth < child.g:
                    deepest_depth = child.g
                    print('deepest search depth', deepest_depth)
                    print('OPEN size: ', len(open_list))
                    print('CLOSED size: ', len(closed_list))
                
if __name__ == "__main__":

    game = Ricochet()
    game.goal = {'color': 'B', 'num': 1, 'row': 5, 'col': 14}
    game.blue["row"] = 2
    game.blue["col"] = 11

    game.red["row"] = 6
    game.red["col"] = 5

    game.yellow["row"] = 11
    game.yellow["col"] = 10

    game.green["row"] = 15
    game.green["col"] = 13

    print(game.goal)
    solve = AStar(game)
    print(solve.agent0)
    print(solve.goal)
    print(solve.path)
    
    