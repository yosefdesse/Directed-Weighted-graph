import unittest
from src.Node import Node


class MyTestCase(unittest.TestCase):

    def test_something(self):
        self.assertNotEqual(True, False)

    def test_get_key(self):
        node = Node(2)
        self.assertEqual(node.get_key(), 2)

    def test_get_pos(self):
        node = Node(1, (0, 0, 0))
        self.assertEqual(node.get_pos(), (0, 0, 0))

    def test_get_tag(self):
        node = Node(2)
        self.assertEqual(node.get_tag(), -1)

    def test_get_distance(self):
        node = Node(2)
        node.set_distance(-2)
        self.assertEqual(node.get_distance(), -2)

    def test_info(self):
        node = Node(1)
        node.set_info("s")
        self.assertEqual(node.info, "s")


if __name__ == '__main__':
    unittest.main()
