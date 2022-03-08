# from ricochet import Ricochet

# b1 = Ricochet()
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

# Python3 Program to print BFS traversal
# from a given source vertex. BFS(int s)
# traverses vertices reachable from s.
from collections import defaultdict

# This class represents a directed graph
# using adjacency list representation
class Graph:

	# Constructor
	def __init__(self):

		# default dictionary to store graph
		self.graph = defaultdict(list)

	def expand(self)
	# Add symetrical edge
	def addSymEdge(self,u,v):
		self.graph[u].append(v)
		self.graph[v].append(u)

	# Function to print a BFS of graph
	def BFS(self, s):

		# Mark all the vertices as not visited
		visited = []
		# Create a queue for BFS
		queue = []

		# Mark the source node as visited and enqueue it
		queue.append(s)
		visited.append(s)

		while queue:
			# Dequeue a vertex from queue and print it
			s = queue.pop(0)
			print (s, end = " ")

			# Get all adjacent vertices of the
			# dequeued vertex s. If a adjacent
			# has not been visited, then mark it
			# visited and enqueue it
			for i in self.graph[s]:
				if i not in visited:
					queue.append(i)
					visited.append(i)

# Driver code

# Create a graph given in
# the above diagram
g = Graph()
g.addSymEdge((b1.yellow["row"], b1.yellow["col"]), )
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

print ("Following is Breadth First Traversal"
				" (starting from vertex 2)")
g.BFS(2)

# This code is contributed by Neelam Yadav
