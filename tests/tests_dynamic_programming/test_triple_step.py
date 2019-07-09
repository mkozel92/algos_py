import unittest

from dynamic_programming.triple_step import triple_step, triple_step_recursion


class TestTripleStep(unittest.TestCase):

    def test_dp_version(self):
        self.assertEqual(triple_step(10), 274)
        self.assertEqual(triple_step(3), 4)

    def test_recursive_version(self):
        mem = {}
        self.assertEqual(triple_step_recursion(10, mem), 274)
        self.assertEqual(triple_step_recursion(3, mem), 4)

    def test_compare(self):
        mem = {}
        for i in range(20):
            self.assertEqual(triple_step(i), triple_step_recursion(i, mem))

