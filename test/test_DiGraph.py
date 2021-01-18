import unittest
from src.Node import Node
from src.edge_data import edge_data
from src.DiGraph import DiGraph


class MyTestCase(unittest.TestCase):
    graph = DiGraph()
    a = Node(1)
    b = Node(2)
    c = Node(3)
    d = Node(4)
    graph.add_node(a.key)
    graph.add_node(b.key)
    graph.add_node(c.key)
    graph.add_node(d.key)

    # def test_get_all_v(self) -> dict:
    #     temp = self.graph.get_all_v().keys()
    #     self.assertEqual(temp, dict_keys([1, 2, 3, 4]))

    def test_add_node(self):
        g = DiGraph()
        g.add_node(3)
        self.assertEqual(g.v_size(), 1)

    def test_remove_node(self):
        g = DiGraph()
        g.add_node(1)
        g.add_node(2)
        g.add_node(3)
        g.add_node(4)
        g.remove_node(4)
        self.assertEqual(g.v_size(), 3)

    def test_get_edge(self):
        g = DiGraph()
        g.add_node(1)
        g.add_node(2)
        g.add_node(3)
        g.add_node(4)
        g.add_edge(1, 2, 3.3)
        g.add_edge(2, 2, 4.4)
        self.assertEqual(g.get_edge(2, 2), 4.4)

    def test_remove_edge(self):
        g = DiGraph()
        g.add_node(1)
        g.add_node(2)
        g.add_node(3)
        g.add_node(4)
        g.add_edge(1, 2, 3.3)
        g.add_edge(2, 2, 4.4)
        g.remove_edge(1,2)
        self.assertEqual(g.get_edge(1, 2),-1)

    def  test_all_in_edges_of_node(self):
        g = DiGraph()
        g.add_node(1)
        g.add_node(2)
        g.add_node(3)
        g.add_edge(1,2,3.3)
        g.add_edge(2,1,3.3)
        g.add_edge(3,1,2.2)
        self.assertEqual(g.all_in_edges_of_node(2), {1:3.3})

    def test_all_out_edges_of_node(self):
        g = DiGraph()
        g.add_node(1)
        g.add_node(2)
        g.add_node(3)
        g.add_node(4)
        g.add_edge(1, 2, 3.3)
        g.add_edge(2, 1, 4.4)
        g.add_edge(3, 2, 4.4)
        g.add_edge(2, 4, 4.4)
        self.assertEqual(g.all_out_edges_of_node(2), {1:4.4, 4:4.4})

    def test_getnode(self):
        g = DiGraph()
        g.add_node(1)
        g.add_node(2)
        g.add_node(3)
        g.add_node(4)
        g.add_edge(1, 2, 3.3)
        g.add_edge(2, 2, 4.4)
        self.assertEqual(g.v_size(),4)

    def test_v_size(self):
        g = DiGraph()
        g.add_node(1)
        g.add_node(2)
        g.add_node(3)
        self.assertEqual(g.v_size(),3)

    def test_mc(self):
        g = DiGraph()
        g.add_node(1)
        g.add_node(2)
        g.add_node(3)
        g.add_edge(1,2,3)
        g.add_edge(2,1,3.3)
        g.remove_edge(1,2)
        self.assertEqual(g.get_mc(),6)


if __name__ == '__main__':
    unittest.main()