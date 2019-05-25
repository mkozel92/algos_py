import unittest

from dynamic_connectivity.quick_find import QuickFind
from dynamic_connectivity.quick_union import QuickUnion
from dynamic_connectivity.weighted_quick_union import WeightedQuickUnion


class TestDynamicConnectivity(unittest.TestCase):

    def setUp(self) -> None:
        self.QF = QuickFind(20)
        self.QU = QuickUnion(20)
        self.WQU = WeightedQuickUnion(20)
        self.dc_objects = [self.QF, self.QU, self.WQU]

    def test_all(self):
        for o in self.dc_objects:
            o.union(1, 2)
            o.union(2, 5)
            o.union(5, 15)
            self.assertTrue(o.connected(1, 15))
            self.assertTrue(o.connected(2, 15))
            self.assertTrue(o.connected(5, 15))
            self.assertFalse(o.connected(1, 10))
            self.assertFalse(o.connected(10, 8))
            self.assertFalse(o.connected(5, 3))

    def test_self_connection(self):
        for o in self.dc_objects:
            self.assertTrue(o.connected(1, 1))
            self.assertTrue(o.connected(2, 2))
            self.assertTrue(o.connected(18, 18))
