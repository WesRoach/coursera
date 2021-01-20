import pytest

import networkx as nx

from lib import (
    cycle_length,
    all_permutations,
    average,
    point_distance,
    complete_undirected_graph,
    nearest_neighbors,
    approximation,
)


# Here is a test case:
# Create an empty graph.
g = nx.Graph()
# Now we will add 6 edges between 4 vertices
g.add_edge(0, 1, weight=2)
# We work with undirected graphs, so once we add an edge from 0 to 1,
# it automatically creates an edge of the same weight from 1 to 0.
g.add_edge(1, 2, weight=2)
g.add_edge(2, 3, weight=2)
g.add_edge(3, 0, weight=2)
g.add_edge(0, 2, weight=1)
g.add_edge(1, 3, weight=1)


@pytest.mark.parametrize(
    "g,cycle,expected",
    [
        (g, [0, 1, 2, 3], 8),
        (g, [0, 2, 1, 3], 6),
    ],  # black .............................................................
)
def test_cycle_length(g, cycle, expected):
    assert expected == cycle_length(g, cycle)


@pytest.mark.parametrize(
    "g,expected",
    [
        (g, 6),
    ],  # black .............................................................
)
def test_all_permutations(g, expected):
    assert expected == all_permutations(g)


@pytest.mark.parametrize(
    "g,expected",
    [
        (g, 6.666666666666667),
    ],  # black .............................................................
)
def test_average(g, expected):
    assert expected == average(g)


@pytest.mark.parametrize(
    "p1,p2,expected",
    [
        ((0, 0), (1, 1), 1.4142135623730951),
        ((-7, -4), (17, 6.5), 26.196373794859472),
    ],  # black ............................................................
)
def test_point_distance(p1, p2, expected):
    assert expected == point_distance(p1, p2)


@pytest.mark.parametrize(
    "points,graph_hash",
    [
        (
            [(174, 25), (129, 99), (268, 212), (211, 209), (156, 82)],
            "b0df24c18b6c07ad010a355fc94f5803",
        )
    ],  # black ............................................................
)
def test_complete_undirected_graph(points, graph_hash):
    g = complete_undirected_graph(points)
    assert graph_hash == nx.weisfeiler_lehman_graph_hash(g)


@pytest.mark.parametrize(
    "coordinates,expected",
    [
        (
            [(174, 25), (129, 99), (268, 212), (211, 209), (156, 82)],
            495.2566051488006,
        ),
    ],  # black .............................................................
)
def test_nearest_neighbors(coordinates, expected):
    g = complete_undirected_graph(coordinates)
    assert expected == nearest_neighbors(g)


@pytest.mark.parametrize(
    "coordinates,expected",
    [
        (
            [(174, 25), (129, 99), (268, 212), (211, 209), (156, 82)],
            495.2566051488006,
        ),
    ],  # black .............................................................
)
def test_approximation(coordinates, expected):
    g = complete_undirected_graph(coordinates)
    assert expected == approximation(g)
