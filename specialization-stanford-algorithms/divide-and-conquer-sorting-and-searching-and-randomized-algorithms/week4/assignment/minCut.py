#!/usr/bin/python

import random, copy
from random import randint
from copy import deepcopy

# open file and create array
fname = '/Users/admin/Dropbox/Learn2Code/Coursera/StanfordAlgorithms/week4/assignment/kargerMinCut.txt'
# fname = '/Users/admin/Dropbox/Learn2Code/Coursera/StanfordAlgorithms/week4/assignment/test1.txt'

# limit = adjList[:int(sys.argv[1])]

adjList = []
nodeList = []
edgeList = []

g = open(fname, 'r')
for line in g:
    values = line.split()
    # print(values)
    # adjList.append((values[0], values[1:]))
    if values:
        values = [int(i) for i in values]
        adjList.append((values[0], values[1:]))

print(adjList)

# create list of all edges
for list in adjList:
    nodeList.append(list[0])
    for edge in list[1]:
        if (edge > list[0]):
            edgeList.append([list[0], edge])

print(edgeList)
print(nodeList)

# karger min cut
def karger(edgeList, nodeList):
    edge_list = deepcopy(edgeList)
    node_list = deepcopy(nodeList)
    while (len(node_list) > 2):
        rand_edge = randint(0, len(edge_list) - 1)
        # print("randInt: {}, target_edge: {}".format(rand_edge, edge_list[rand_edge]))
        target_edge = edge_list[rand_edge]
        replace_with = target_edge[0]
        should_replace = target_edge[1]
        for edge in edge_list:
            if (edge[0] == should_replace):
                edge[0] = replace_with
            if (edge[1] == should_replace):
                edge[1] = replace_with
        # edge_list.remove(target_edge)
        node_list.remove(should_replace)
        for i in range(len(edge_list)-1,-1,-1):
            if edge_list[i][0] == edge_list[i][1]:
                edge_list.remove(edge_list[i])

        # print(edge_list)

    return [len(edge_list), node_list, edge_list]

# repeat karger xx times and return min cuts
min_cut = karger(edgeList, nodeList)
for i in range(0, 200):
    ret = karger(edgeList, nodeList)
    print(ret)
    if ret[0] < min_cut[0]:
        min_cut = ret

print('break')
print(min_cut)













# print(len(adjList))

# while (len(adjList) > 2):
# pick random node, delete random Edge, follow Edge, Delete Edge in connecting
# with open(fname) as req_file:
#     mincut_data = []
#     for line in req_file:
#         line = line.split()
#         if line:
#             line = [int(i) for i in line]
#             mincut_data.append(line)
#
# #extracting edges from the data #
# edgelist = []
# nodelist = []
# for every_list in mincut_data:
#     nodelist.append(every_list[0])
#     temp_list = []
#     for temp in range(1,len(every_list)):
#         temp_list = [every_list[0], every_list[temp]]
#         flag = 0
#         for ad in edgelist:
#             if set(ad) == set(temp_list):
#                 flag = 1
#         if flag == 0 :
#             edgelist.append([every_list[0],every_list[temp]])
#
# print(edgelist)
# print(nodelist)