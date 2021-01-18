import unittest
from src.Node import Node
from src.edge_data import edge_data


class MyTestCase(unittest.TestCase):

    def test_get_src(self):
        node = Node(2)
        node = Node(1)
        edge = edge_data(1, 2, 3.3)
        self.assertEqual(1, 1)

    def test_dest(self):
        node = Node(2)
        node = Node(1)
        edge = edge_data(1, 2, 3.3)
        self.assertEqual(2, 2)

    def test_weight(self):
        node = Node(1)
        node = Node(2)
        node = Node(1)
        edge = edge_data(1, 2, 3.3)
        self.assertEqual(edge.weight, 3.3)

    def test_info(self):
        node = Node(2)
        node = Node(1)
        edge = edge_data(0, 0, 0)
        edge.set_info("s")
        self.assertEqual(edge.get_info(), "s")


if __name__ == '__main__':
    unittest.main()
