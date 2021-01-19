# %load_ext autoreload
# %autoreload 2

import networkx as nx
import math
from itertools import permutations, combinations

from lib import point_distance, complete_undirected_graph

242.10122702547523 * 2

points = [(174, 25), (129, 99), (268, 212), (211, 209), (156, 82)]
points

g = complete_undirected_graph(points)

n = 3

for v in g.nodes():
    if v == n:
        continue
    print(v)

g.edges()

g[0][1]['weight']

points = [(idx, t) for idx, t in enumerate(points)]
points

comb = [x for x in combinations(points, 2)]
comb

for c in comb:
    print(c[0][1][0], c[0][1][1])

g = nx.Graph()

for c in comb:
    idx1 = c[0][0]
    idx2 = c[1][0]
    p1 = c[0][1]
    p2 = c[1][1]
    g.add_edge(idx1, idx2, weight=point_distance(p1, p2))

g.nodes()

g.edges()

g.degree()

nx.weisfeiler_lehman_graph_hash(g)

g[0][1]["weight"]





g = nx.Graph()

for idx, point in enumerate(points):
    g.add_node(idx, pos=point)

g.nodes()

g.get_edge_pos()
