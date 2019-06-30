import unittest
from binary_tree_algos.binary_tree import BinaryTree
from binary_tree_algos.common_ancestor import common_ancestor


class TestCommonAncestor(unittest.TestCase):

    def setUp(self) -> None:
        self.bt = BinaryTree()
        self.bt.put(5, '')
        self.bt.put(8, '')
        self.bt.put(2, '')
        self.bt.put(6, '')
        self.bt.put(9, '')
        self.bt.put(1, '')
        self.bt.put(3, '')

    def test_common_ancestor(self):
        root = self.bt.root
        a = root.right
        b = root.left
        _, _, c = common_ancestor(a, b, root)
        self.assertEqual(c, root)

        a = root.right.right
        b = root.right.left
        _, _, c = common_ancestor(a, b, root)
        self.assertEqual(c, root.right)

        a = root.left.right
        b = root.left
        _, _, c = common_ancestor(a, b, root)
        self.assertEqual(c, root.left)
