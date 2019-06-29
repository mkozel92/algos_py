import unittest

from stacks_and_queues.queue_by_stacks import QueueByStacks


class TestQueueByStacks(unittest.TestCase):

    def test_queue_by_stacks(self):
        qbs = QueueByStacks()
        qbs.enqueue(1)
        qbs.enqueue(2)
        qbs.enqueue(3)
        qbs.enqueue(4)

        self.assertEqual(qbs.dequeue(), 1)
        self.assertEqual(qbs.dequeue(), 2)
        self.assertEqual(qbs.dequeue(), 3)

        qbs.enqueue(5)
        qbs.enqueue(6)
        qbs.enqueue(7)

        self.assertEqual(qbs.dequeue(), 4)
        self.assertEqual(qbs.dequeue(), 5)
        self.assertEqual(qbs.dequeue(), 6)
