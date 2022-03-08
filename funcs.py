from collections import defaultdict
from ricochet import Ricochet
import copy
import pdb

b1 = Ricochet()
# print(b1.board)
# print(b1.yellow)
# print('\n')
# print(b1.availableMoves(b1.yellow))
# b1.yellow["row"] = 0
# b1.yellow["col"] = 1
# b1.board[0, :] = "S"
# print(b1.availableMoves(b1.yellow))
# print("")
# b1.move(b1.yellow,'UP')
# print(b1.board)
#for i in range(10):

goal = ((b1.goal["row"], b1.goal["col"]))
print("Goal: ", goal)
g = defaultdict(list)

root = copy.deepcopy(b1)
print(root.yellow)
print(root.availableMoves(root.yellow))
# Create list for visited and queue
visited = []
queue = []
path = {}

# Mark the source node as visited and enqueue it
root_pos = (root.yellow["row"], root.yellow["col"])
queue.append(root_pos)
visited.append(root_pos)
path[root_pos] = []

for i in range(10):
    print(i)
    pos = queue.pop(0)
    root.yellow['row'] = pos[0]
    root.yellow['col'] = pos[1]
    for dir in ['UP', 'DOWN', 'LEFT', 'RIGHT']:
        move_dir = root.availableMoves(root.yellow)[dir]
        print(move_dir)
        if move_dir not in visited:
            if move_dir == goal:
                print("FOUND GOAL!!!!")
                path[move_dir] = path[pos].copy()
                path[move_dir].append(dir)
                print(move_dir)
                print(path[move_dir])
                break
            g[pos].append(move_dir)
            g[move_dir].append(pos)
            queue.append(move_dir)
            visited.append(move_dir)
            #pdb.set_trace()
            path[move_dir] = path[pos].copy()
            path[move_dir].append(dir)
    if move_dir == goal: break
#    root.move(root.yellow,'UP')
#pdb.set_trace()








# #Expand nodes
# #If not visited visit and add to queue

# 		# Mark all the vertices as not visited
# 		visited = []
# 		# Create a queue for BFS
# 		queue = []

# 		# Mark the source node as visited and enqueue it
# 		pos = (root.yellow["row"], root.yellow["col"])
# 		queue.append(pos)
# 		visited.append(pos)

# 		while queue:
# 			# Dequeue a vertex from queue and print it
# 			s = queue.pop(0)
# 			print (s, end = " ")

# 			# Get all adjacent vertices of the
# 			# dequeued vertex s. If a adjacent
# 			# has not been visited, then mark it
# 			# visited and enqueue it
# 			for i in self.graph[s]:
# 				if i not in visited:
# 					queue.append(i)
# 					visited.append(i)