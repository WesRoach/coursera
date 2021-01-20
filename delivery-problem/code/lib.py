import networkx as nx
import math
from itertools import permutations, chain, combinations


def cycle_length(g, cycle):
    """
    Quiz: Cycle Weight
    ------------------

    This function takes as input a graph g and a list of vertices of
    the cycle. (Each vertex given by its index starting from 0.)
    The graph is complete (i.e., each pair of distinct vertices is
    connected by an edge), undirected (i.e., the edge from u to v has
    the same weight as the edge from v to u), and has no self-loops
    (i.e., there are no edges from i to i).

    For example, a valid input would be a graph on 3 vertices and
    cycle = [2, 0, 1].

    The function should return the weight of the cycle.
    (Don't forget to add up the last edge connecting the last vertex
    of the cycle with the first one.)

    If you want to get the weight of the edge between vertices u and v,
    you can take g[u][v]['weight']
    """

    # Checking that the number of vertices in the graph equals the number of vertices in the cycle.
    assert len(cycle) == g.number_of_nodes()

    length = 0
    for i in range(0, len(cycle)):
        length += g[cycle[i]][cycle[(i + 1) % len(cycle)]]["weight"]

    return length


def all_permutations(g):
    """
    Quiz: Brute Force
    -----------------

    This function takes as input a graph g.

    The graph is complete (i.e., each pair of distinct vertices is
    connected by an edge), undirected (i.e., the edge from u to v
    has the same weight as the edge from v to u), and has no
    self-loops (i.e., there are no edges from i to i).

    The function should return the weight of a shortest Hamiltonian cycle.
    (Don't forget to add up the last edge connecting the last vertex
    of the cycle with the first one.)

    You can iterate through all permutations of the set {0, ..., n-1}
    and find a cycle of the minimum weight.
    """
    # n is the number of vertices.
    n = g.number_of_nodes()

    # Iterate through all permutations of n vertices
    smallest_length = None
    for p in permutations(range(n)):
        length = cycle_length(g, p)
        if smallest_length is None or length < smallest_length:
            smallest_length = length

    return smallest_length


def average(g):
    """
    Quiz: Average Weight
    --------------------

    This function takes as input a graph g.

    The graph is complete (i.e., each pair of distinct vertices is
    connected by an edge), undirected (i.e., the edge from u to v
    has the same weight as the edge from v to u), and has no self-loops
    (i.e., there are no edges from i to i).

    The function should return the average weight of a Hamiltonian cycle.
    (Don't forget to add up the last edge connecting the last vertex of
    the cycle with the first one.)
    """
    # n is the number of vertices.
    n = g.number_of_nodes()

    # Sum of weights of all n*(n-1)/2 edges.
    sum_of_weights = sum(g[i][j]["weight"] for i in range(n) for j in range(i))

    # Write your code here.
    return (sum_of_weights / (n - 1)) * 2


def point_distance(p1: tuple, p2: tuple) -> float:
    """Returns distance between two points on 2D plane."""
    return math.sqrt(((p2[0] - p1[0]) ** 2) + ((p2[1] - p1[1]) ** 2))


def complete_undirected_graph(points: list) -> nx.Graph:
    """
    Given list of points, create a graph.
    """
    # add indices to points
    points = [(idx, t) for idx, t in enumerate(points)]
    g = nx.Graph()
    for edge in [x for x in combinations(points, 2)]:
        idx1 = edge[0][0]
        idx2 = edge[1][0]
        p1 = edge[0][1]
        p2 = edge[1][1]
        g.add_edge(idx1, idx2, weight=point_distance(p1, p2))
    return g


def nearest_neighbors(g):
    """
    Quiz: Nearest Neighbor
    ----------------------

    This function takes as input a graph g.

    The graph is complete (i.e., each pair of distinct vertices is
    connected by an edge), undirected (i.e., the edge from u to v
    has the same weight as the edge from v to u), and has no
    self-loops (i.e., there are no edges from i to i).

    The function should return the weight of the nearest neighbor
    heuristic, which starts at the vertex number 0, and then each
    time selects a closest vertex.
    """
    current_node = 0
    path = [current_node]
    n = g.number_of_nodes()

    # We'll repeat the same routine (n-1) times
    for _ in range(n - 1):
        next_node = None
        # The distance to the closest vertex. Initialized with infinity.
        min_edge = float("inf")
        for v in g.nodes():
            # Write your code here: decide if v is a better candidate than
            # next_node. If it is, then update the values of next_node and
            # min_edge
            if current_node == v or v in path:
                continue
            elif next_node is None:
                next_node = v
                min_edge = g[current_node][v]["weight"]
            elif g[current_node][v]["weight"] < min_edge:
                min_edge = g[current_node][v]["weight"]
                next_node = v

        assert next_node is not None
        path.append(next_node)
        current_node = next_node

    weight = sum(
        g[path[i]][path[i + 1]]["weight"]
        for i in range(g.number_of_nodes() - 1)
    )
    weight += g[path[-1]][path[0]]["weight"]
    return weight


def lower_bound(g, sub_cycle):
    """
    Quiz: Branch and Bound
    ----------------------

    This function computes a lower bound on the length of Hamiltonian
    cycles starting with vertices in the list sub_cycle.

    I would recommend to first see the branch_and_bound function below,
    and then return to lower_bound.
    """
    # The weight of the current path.
    current_weight = sum(
        [
            g[sub_cycle[i]][sub_cycle[i + 1]]["weight"]
            for i in range(len(sub_cycle) - 1)
        ]
    )

    # For convenience we create a new graph which only contains vertices not
    # used by g.
    unused = [v for v in g.nodes() if v not in sub_cycle]
    h = g.subgraph(unused)

    # Compute the weight of a minimum spanning tree.
    t = list(nx.minimum_spanning_edges(h))
    mst_weight = sum([h.get_edge_data(e[0], e[1])["weight"] for e in t])

    # If the current sub_cycle is "trivial" (i.e., it contains no
    # vertices or all vertices), then our lower bound is just the sum
    # of the weight of a minimum spanning tree and the current weight.
    if len(sub_cycle) == 0 or len(sub_cycle) == g.number_of_nodes():
        return mst_weight + current_weight

    # If the current sub_cycle is not trivial, then we can also add
    # the weight of two edges connecting the vertices from sub_cycle
    # and the remaining part of the graph.
    # s is the first vertex of the sub_cycle
    s = sub_cycle[0]
    # t is the last vertex of the sub_cycle
    t = sub_cycle[-1]
    # The minimum weight of an edge connecting a vertex from outside of
    # sub_sycle to s.
    min_to_s_weight = min(
        [g[v][s]["weight"] for v in g.nodes() if v not in sub_cycle]
    )
    # The minimum weight of an edge connecting the vertex t to a vertex from
    # outside of sub_cycle.
    min_from_t_weight = min(
        [g[t][v]["weight"] for v in g.nodes() if v not in sub_cycle]
    )

    # Any cycle which starts with sub_cycle must be of length:
    # the weight of the edges from sub_cycle
    # + minimum weight of an edge connecting sub_cycle and the remaining vertices
    # + minimum weight of a spanning tree on the remaining vertices
    # + minimum weight of an edge connecting the remaining vertices to sub_cycle
    return current_weight + min_from_t_weight + mst_weight + min_to_s_weight


def branch_and_bound(g, sub_cycle=None, current_min=float("inf")):
    """
    Quiz: Branch and Bound
    ----------------------

    Arguments
    ---------
        g: a graph
        sub_cycle: several first vertices of cycle under
            consideration.
            Initially sub_cycle is empty
        current_min: current best solution, so that we don't even
            consider paths of greater weight.
            Initially the min weight is infinite
    """
    # If the current path is empty, then we can safely assume that it starts
    # with the vertex 0.
    if sub_cycle is None:
        sub_cycle = [0]

    # If we already have all vertices in the cycle, then we just compute the
    # weight of this cycle and return it.
    if len(sub_cycle) == g.number_of_nodes():
        weight = sum(
            [
                g[sub_cycle[i]][sub_cycle[i + 1]]["weight"]
                for i in range(len(sub_cycle) - 1)
            ]
        )
        weight = weight + g[sub_cycle[-1]][sub_cycle[0]]["weight"]
        return weight

    # Now we look at all nodes which aren't yet used in sub_cycle.
    unused_nodes = list()
    for v in g.nodes():
        if v not in sub_cycle:
            unused_nodes.append((g[sub_cycle[-1]][v]["weight"], v))

    # We sort them by the distance from the "current node" -- the last node
    # in sub_cycle.
    unused_nodes = sorted(unused_nodes)

    for (d, v) in unused_nodes:
        assert v not in sub_cycle
        extended_subcycle = list(sub_cycle)
        extended_subcycle.append(v)
        # For each unused vertex, we check if there is any chance to find a
        # shorter cycle if we add it now.
        if lower_bound(g, extended_subcycle) < current_min:
            # WRITE YOUR CODE HERE
            # If there is such a chance, we add the vertex to the current
            # cycle, and proceed recursively. If we found a short cycle, then
            # we update the current_min value.
            this_min = branch_and_bound(g, sub_cycle, current_min)
            if this_min < current_min:
                current_min = this_min

    # The procedure returns the shortest cycle length.
    return current_min


def dp(G):
    """
    Alexander S. Kulikov discusses in lecture.

    - Running time is about (n^2)*(2^n)
    - Better than n!, but still too slow (already for n=20)
    """
    n = G.number_of_nodes()
    T = [[float("inf")] * (1 << n) for _ in range(n)]
    T[0][1] = 0
    for s in range(1 << n):
        if sum(((s >> j) & 1) for j in range(n)) <= 1 or not (s & 1):
            continue

    for i in range(1, n):
        if not ((s >> i) & 1):
            continue
        for j in range(n):
            if j == i or not ((s >> j) & 1):
                continue

            T[i][s] = min(T[i][s], T[j][s ^ (1 << i)] + G[i][j]["weight"])

    return min(T[i][(1 << n) - 1] + G[0][i]["weight"] for i in range(1, n))


def powerset(s):
    """
    Quiz: Dynamic Programming
    -------------------------

    This function returns all the subsets of the given set s in the
    increasing order of their sizes.
    """
    return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))


def dynamic_programming(g):
    """
    Quiz: Dynamic Programming
    -------------------------

    This function finds an optimal Hamiltonian cycle using the dynamic
    programming approach.

    This function takes as input a graph g.
    The graph is complete (i.e., each pair of distinct vertices is
    connected by an edge), undirected (i.e., the edge from u to v has
    the same weight as the edge from v to u), and has no self-loops
    (i.e., there are no edges from i to i).

    The function should return an optimal weight of a Hamiltonian cycle.
    """
    # n is the number of vertices.
    n = g.number_of_nodes()

    # The variable power now contains a tuple for each subset of the set
    # {1, ..., n-1}.
    power = powerset(range(1, n))
    # The variable T is a dictionary, where the element T[s, i] for a set s
    # and an integer i equals the shortest path going through each vertex from
    # s exactly once, and ending at the vertex i.
    # Note that i must be in s.
    # Also, always assume that we start our cycle from the vertex number 0.
    # Thus, for convenience, we always exclude the element 0 from the set s.
    T = {}
    # For every non-zero vertex i, we say that
    # T[ tuple with the element i only, i] equals the weight of the edge
    # from 0 to i.
    # Indeed, by the definition of T, this element must be equal to the weight
    # of the shortest path which goes through the vertices 0 and i and ends at
    # the vertex i.
    for i in range(1, n):
        # Syntactic note: In Python, we define a tuple of length 1 that
        # contains the element i as (i,) *with comma*.
        T[(i,), i] = g[0][i]["weight"]

    # For every subset s of [1,...,n-1]
    for s in power:
        # We have already initialized the elements of T indexed by sets of size
        # 1, so we skip them.
        if len(s) > 1:
            # For every vertex i from s which we consider as the ending vertex
            # of a path going through vertices from s.
            for i in s:
                # Define the tuple which contains all elements from s without
                # *the last vertex* i.
                t = tuple([x for x in s if x != i])
                # Now we compute the optimal value of a cycle which visits all
                # vertices from s and ends at the vertex i.

                T[s, i] = float("inf")
                for j in s:
                    if j == i:
                        continue
                    T[s, i] = min(T[s, i], T[t, j] + g[i][j]["weight"])

    # Return the weight of on optimal cycle - this is the minimum of the
    # following sum:
    # weight of a path + the last edge to the vertex 0.
    return min(
        T[tuple(range(1, n)), i] + g[i][0]["weight"] for i in range(1, n)
    )


def approximation(g):
    """
    This function takes as input a graph g.

    The graph is complete (i.e., each pair of distinct vertices is
    connected by an edge), undirected (i.e., the edge from u to v has
    the same weight as the edge from v to u), and has no self-loops
    (i.e., there are no edges from i to i).

    The function should return a 2-approximation of an optimal
    Hamiltonian cycle.
    """
    # n is the number of vertices.
    n = g.number_of_nodes()

    # You might want to use the function "nx.minimum_spanning_tree(g)"
    # which returns a Minimum Spanning Tree of the graph g
    mst = nx.minimum_spanning_tree(g)

    # You also might want to use the command
    # "list(nx.dfs_preorder_nodes(graph, 0))" which gives a list of vertices of
    # the given graph in depth-first preorder.
    dfs = list(nx.dfs_preorder_nodes(mst, 0))

    weight = 0
    for i in range(0, len(dfs)):
        weight += g[dfs[i]][dfs[(i + 1) % len(dfs)]]["weight"]

    return weight
