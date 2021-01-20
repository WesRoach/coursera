# %load_ext autoreload
# %autoreload 2

import networkx as nx
import math
from itertools import permutations, combinations

from lib import point_distance, complete_undirected_graph

points = [(174, 25), (129, 99), (268, 212), (211, 209), (156, 82)]
points

g = complete_undirected_graph(points)

nx.draw_networkx(g)

n = g.number_of_nodes()

T = nx.minimum_spanning_tree(g)

nx.draw_networkx(T)

ECycle = nx.eulerian_path(T)

[x for x in ECycle]

lst = nx.dfs_preorder_nodes(T, 0)

[x for x in lst]


