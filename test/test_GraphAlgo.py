import unittest

from src.DiGraph import DiGraph
from src.GraphAlgo import GraphAlgo


class MyTestCase(unittest.TestCase):

    def test_shortpath(self):
        graph = DiGraph()
        graph.add_node(0)
        graph.add_node(1)
        graph.add_node(2)
        graph.add_node(3)
        graph.add_node(4)
        graph.add_node(5)
        graph.add_node(6)
        graph.add_edge(0, 1, 3)
        graph.add_edge(0, 3, 10)
        graph.add_edge(0, 2, 2)
        graph.add_edge(1, 6, 2)
        graph.add_edge(6, 3, 1)
        graph.add_edge(2, 4, 12)
        graph.add_edge(2, 5, 4)
        graph.add_edge(5, 4, 4)
        graph.add_edge(5, 3, 8)
        g_algo = GraphAlgo(graph)
        d, c = g_algo.shortest_path(0, 3)
        self.assertEqual(c, [0, 1, 6, 3])
        self.assertEqual(d, 6)

    def test_connected_components(self):
        graph = DiGraph()
        graph.add_node(0)
        graph.add_node(1)
        graph.add_node(2)
        graph.add_node(3)
        graph.add_node(4)
        graph.add_node(5)
        graph.add_node(6)
        graph.add_node(7)
        graph.add_edge(0, 1, 2)
        graph.add_edge(1, 2, 2)
        graph.add_edge(2, 0, 2)
        graph.add_edge(5, 0, 2)
        graph.add_edge(5, 6, 2)
        graph.add_edge(6, 2, 2)
        graph.add_edge(6, 0, 2)
        graph.add_edge(6, 4, 2)
        graph.add_edge(4, 5, 2)
        graph.add_edge(3, 4, 2)
        graph.add_edge(3, 7, 2)
        graph.add_edge(7, 3, 2)
        graph.add_edge(7, 5, 2)
        g_algo = GraphAlgo(graph)
        answer = [[0, 1, 2], [3, 7], [4, 5, 6]]
        self.assertEqual(g_algo.connected_components(), answer)

    def test_connected_component(self):
        graph = DiGraph()
        graph.add_node(0)
        graph.add_node(1)
        graph.add_node(2)
        graph.add_node(3)
        graph.add_node(4)
        graph.add_node(5)
        graph.add_node(6)
        graph.add_node(7)
        graph.add_edge(0, 1, 2)
        graph.add_edge(1, 2, 2)
        graph.add_edge(2, 0, 2)
        graph.add_edge(5, 0, 2)
        graph.add_edge(5, 6, 2)
        graph.add_edge(6, 2, 2)
        graph.add_edge(6, 0, 2)
        graph.add_edge(6, 4, 2)
        graph.add_edge(4, 5, 2)
        graph.add_edge(3, 4, 2)
        graph.add_edge(3, 7, 2)
        graph.add_edge(7, 3, 2)
        graph.add_edge(7, 5, 2)
        g_algo = GraphAlgo(graph)
        answer = [0, 1, 2]
        self.assertEqual(g_algo.connected_component(1), answer)


if __name__ == '__main__':
    unittest.main()
