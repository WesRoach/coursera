#!/Users/admin/anaconda/bin/python


# The file contains the edges of a directed graph. Vertices are labeled as positive integers from 1 to 875714. Every row indicates an edge, the vertex label in first column is the tail and the vertex label in second column is the head (recall the graph is directed, and the edges are directed from the first column vertex to the second column vertex). So for example, the 11th row looks liks : "2 47646". This just means that the vertex with label 2 has an outgoing edge to the vertex with label 47646

# Your task is to code up the algorithm from the video lectures for computing strongly connected components (SCCs), and to run this algorithm on the given graph.

# Output Format: You should output the sizes of the 5 largest SCCs in the given graph, in decreasing order of sizes, separated by commas (avoid any spaces). So if your algorithm computes the sizes of the five largest SCCs to be 500, 400, 300, 200 and 100, then your answer should be "500,400,300,200,100" (without the quotes). If your algorithm finds less than 5 SCCs, then write 0 for the remaining terms. Thus, if your algorithm computes only 3 SCCs whose sizes are 400, 300, and 100, then your answer should be "400,300,100,0,0" (without the quotes). (Note also that your answer should not have any spaces in it.)

# WARNING: This is the most challenging programming assignment of the course. Because of the size of the graph you may have to manage memory carefully. The best way to do this depends on your programming language and environment, and we strongly suggest that you exchange tips for doing this on the discussion forums.

import sys
from copy import deepcopy

# fname = '/Users/admin/Dropbox/Learn2Code/Coursera/StanfordAlgorithms/week5/assignment/SCC.txt'
fname = '/Users/admin/Dropbox/Learn2Code/Coursera/StanfordAlgorithms/week5/assignment/test1.txt'

# list of each edge
edgeList = []
adjList = []

# track max value of max node
maxNodeNum = 0

g = open(fname)
# edgeList
for line in g:
    u = int(line.split()[0])
    v = int(line.split()[1])
    edgeList.append([u, v])
    # determine max V number
    if u > maxNodeNum: maxNodeNum = u
    elif v > maxNodeNum: maxNodeNum = v

print(edgeList)
print(maxNodeNum)

# array with value x for each V
# [vertex, firstVisted, firstFinish,
# vertList = [ [x, 0, None] for x in range(0, maxNodeNum + 1) ]
# print(vertList)

# build adjacency list from vectList & edgeList
# for V in range(0, maxNodeNum + 1):
#     adjList.append([V, []])
# for edge in edgeList:
#     adjList[edge[0]][1].append(edge[1])
# print(adjList)

# Test adjList->edgeList
# for V in adjList:
#     for edge in V[1]:
#         print((V[0],edge))

# edgeList is a list of each edge
# adjList is a list of each Vertex and the other Vertex(s) it points to
# vertList is a list of each Vertex, and if it's been visited

# class Graph(edgeList, maxNodeNum):
class Graph():

    def __init__(self):
        #     [Vertex, firstVisited, finTime, secondVisited leader]
        self.vertList = [ [x, 0, 0, 0] for x in range(0,
                                                                maxNodeNum +
                                                           1) ]
        self.adjList = []
        self.adjListRev = []
        self.numVertex = maxNodeNum

        # build adjList for natural graph
        for V in range(0, maxNodeNum + 1):
            self.adjList.append([V, []])
        for edge in edgeList:
            self.adjList[edge[0]][1].append(edge[1])

        # build adjListRev for Grev
        for V in range(0, maxNodeNum + 1):
            self.adjListRev.append([V, []])
        for edge in edgeList:
            self.adjListRev[edge[1]][1].append(edge[0])

g = Graph()
print("vertList [Vertex, firstVisited, finTime, secondVisited, leader]:\n",
      g.vertList)
print("g.adjList:\n", g.adjList)
print("g.adjListRev:\n", g.adjListRev)

t = 0
s = None

# entry to DFS - takes a graph object
def DFS_Loop(G):
    global s, t
    # Move through adjListRev from maxVertex to minVertex
    for i in range(G.numVertex, 1, -1):
        if G.vertList[i][1] == 0: # Vertex unexplored
            s = G.vertList[i][0]
            DFS(G,i)

def DFS(G, i):
    global s, t
    G.vertList[i][1] = 1
    # set leader = s
    G.vertList[i][3] = s
    # leader = s
    for p in G.adjListRev[i][1]: # i = current Vertex; p = iterative point
        if G.vertList[p][1] == 0:
            DFS(G, p)
    t+=1
    G.vertList[i][2] = t
    # G.vertList[i][3] = leader

DFS_Loop(g)

print("## First Pass")
# sort vertList by finishing times
g.vertList = sorted(g.vertList, key=lambda x: x[2])
# reset visited flag
for vert in g.vertList:
    vert[1] = 0
print("vertList [Vertex, firstVisited, finTime, leader]:\n", g.vertList)
print("g.adjList:\n", g.adjList)
print("g.adjListRev:\n", g.adjListRev)


# print(g.vertList)

DFS_Loop(g)

print("## Second Pass")
print("vertList [Vertex, firstVisited, finTime, leader]:\n", g.vertList)





# sort vertList by finishing time

## Notes
# DFS-Loop(graph G)
#   mark all nodes unexplored
#   current-label = n  (to keep track of ordering)

# for each vertex
#     if v not yet explored (in previous DFS call)
#         DFS(G, v)

# DFS(graph G, start vertex s)
#     for every edge (s,v)
#         if v not yet explored
#             mark v explored
#             DFS(G, v)
#     set f(s) = current_label
#     current_label = current_label - 1

# Kosaraju's Two-Pass Algorithm
# 1) Let Grev = G with all arvs reversed
# 2) Run DFS-Loop on Grev (Goal: computer "magical ordering" of nodes)
#     Let f(v) = "finishing time" of each V in V
# 1) Run DFS-Loop on G (Goal: discover the SCCs one-by-one)
#     processing nodes in decreasing order of finishing times
# [SCCs = nodes with the same "leader"]

## DFS-Loop
# DFS-Loop(graph G)
#   Global variable t = 0 (For finishing times in 1st pass)
#       [# of nodes processed so far]
#   Global variable s = NULL (For leaders in 2nd pass)
#       [current source vertex]
#   Assume nodes labeled 1 to n
#   For i = n down to 1
#       if i not yet explored
#           s = i
#           DFS(G, i)
#
# DFS(graph G, node i)
#     mark i as explored (For rest of DFS-Loop)
#     set leader(i) = node s
#     for each arc(i,j) in G
#         if j not yet explored
#             DFS(G, j)
#     t++
#     set f(i) = t (i's finishing time)













