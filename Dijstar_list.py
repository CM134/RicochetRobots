from Heuristics import Heuristics
from ricochet import Ricochet
import copy
import time


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


class Dijkstra:
    def __init__(self, game):
        self.colorMap = {'R': 'red', 'Y': 'yellow', 'G': 'green', 'B': 'blue'}
        self.goal = game.goal
        self.board = game.board
        self.game = copy.deepcopy(game)
        self.color = self.colorMap[self.goal['color']]
        rest_colors = list(self.colorMap.values())
        rest_colors.remove(self.color)
        # Add other robots
        self.agent0 = getattr(self.game, self.color)
        for i in range(3):
            setattr(self, ("agent"+str(i+1)),
                    getattr(self.game, rest_colors[i]))
        H = Heuristics(game)
        self.h_goal = H.goal_matrix
        self.h_other = H.other_matrix

        self.path = self.dijkstra()

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

    def dijkstra(self):
        """Returns a list of tuples as a path from the given start to the given end in the given maze"""
        deepest_depth = 0
        # Create start
        root_pos = self.getPoses()
        goal = ((self.goal["row"], self.goal["col"]))
        start_node = Node(None, root_pos)
        start_node.g = start_node.h = start_node.f = 0

        # Initialize both open and closed list
        node_list = []

        queue_pos = []
        queue_f = []
        visited_pos = []

        # Add the start node
        node_list.append(start_node)
        queue_pos.append(root_pos)
        queue_f.append(0)

        # Loop until you find the end or 1 minute passes without a solution
        time0 = time.time()
        while ((time.time()-time0) < 60) and len(queue_pos) > 0:

            # Get the current node with lowest f
            current_pos = queue_pos[0]
            current_f = queue_f[0]
            current_index = 0
            for index in range(len(queue_pos)):
                if queue_f[index] < current_f:
                    current_index = index
                    current_f = queue_f[index]


            # Pop current off open list, add to closed list
            current_f = queue_f.pop(current_index)
            current_pos = queue_pos.pop(current_index)
            
            # closed_list.append(current_node)
            visited_pos.append(current_pos)
            
            #get current node for goal check
            for i in range(len(node_list)):
                loop_node = node_list[i]
                if loop_node.position == current_pos:
                    current_node = loop_node

            # Found the goal
            if current_pos[0] == goal:
                path = []
                current = current_node
                while current is not None:
                    path.append((current.color,current.move))
                    current = current.parent
                path = path[::-1] # Return reversed path
                return path [1:] # fist argument of path is '',''. We want to skip that.


            # Generate children:
            # iterate through robots and each possible robot move
            node_children = []
            children_pos = []
            children_agent = []
            pos = current_pos
            for i in range(4):  # Adjacent squares
                self.setPoses(pos)  # Resets all poses to queue start positions
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
                    agent_nr = i
                    new_node.move = dir
                    new_node.color = self.colorMap[ag['name']]

                    if new_pos not in visited_pos:
                        if new_pos in queue_pos:
                            # compare g
                            idx = queue_pos.index(new_pos) # fails if node not in list
                            if agent_nr == 0:
                                new_f = self.h_goal[new_pos[agent_nr]]
                            else:
                                new_f = self.h_goal[new_pos[agent_nr]]
                            
                            open_f = queue_f[idx]
                            if open_f > new_f:
                                queue_f.pop(idx)
                                queue_pos.pop(idx)
                                
                                node_children.append(new_node)
                                
                                children_pos.append(new_pos)
                                children_agent.append(agent_nr)
                        else:
                            node_children.append(new_node)
                            children_pos.append(new_pos)
                            children_agent.append(agent_nr)
            
            # # Loop through children
            # for child in children:
            #     # Create the f, g, and h values

            #     child.g = current_node.g + 1   # comment this and you get greedy search
            #     if child.agent_nr == 0:
            #         child.h = self.h_goal[child.position[0]]
            #     else:
            #         child.h = self.h_other[child.position[child.agent_nr]]
            #     child.f = child.h

            #     # Add the child to the open list
            #     open_list.append(child)

            #     if deepest_depth < child.g:
            #         deepest_depth = child.g
            #         print('deepest search depth', deepest_depth)
            #         print('OPEN size: ', len(open_list))
            #         print('CLOSED size: ', len(closed_list))
                    
                    
            # # Loop through children
            for index, child in enumerate(children_pos):

                # Create the f, g, and h values
                            
                if children_agent[index] == 0:
                    h = self.h_goal[child[0]]
                else:
                    h = self.h_other[child[children_agent[index]]]
                f = h

                # Add the child to the open list
                # open_list.append(child)
                queue_f.append(f)
                queue_pos.append(child)
            
                # if deepest_depth < queue_g[-1]:
                #     deepest_depth = queue_g[-1]
                #     print('deepest search depth', deepest_depth)
                #     print('OPEN size: ', len(queue_pos))
                #     print('CLOSED size: ', len(visited_pos))
                
            # append all the node children
            for i in range(len(node_children)):
                loop_node = node_children[i]
                loop_node.g = current_node.g +1
                node_list.append(loop_node)
                
                if deepest_depth < loop_node.g:
                    deepest_depth = loop_node.g
                    print('deepest search depth', deepest_depth)
                    print('OPEN size: ', len(queue_pos))
                    print('CLOSED size: ', len(visited_pos))
                    
                    
        return None  # Return None as path if unable to find within constrains


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
    solve = Dijkstra(game)
    print(solve.agent0)
    print(solve.goal)
    print(solve.path)
