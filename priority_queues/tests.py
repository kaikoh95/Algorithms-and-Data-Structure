"""Module containing the unit tests for all questions."""
import unittest
import random
import string
from top_k import top_k_select, top_k_heap
from basic_priority_queue import BasicPriorityQueue
from change_priority_queue import ChangePriorityQueue
from dheap_priority_queue import DheapPriorityQueue
from fast_priority_queue import FastPriorityQueue

class TestTopK(unittest.TestCase):
    """Tests for Task 1 on finding the top k items."""

    def test_top_k_select(self):
        """Tests the top_k_select function on a list of 1000 integers."""
        test_data = list(range(1000))
        random.shuffle(test_data)
        top_40, _ = top_k_select(test_data, 40)
        self.assertEqual(top_40, list(range(999, 959, -1)))

    def test_top_k_select_comparisons(self):
        """Tests the number of comparisons the top_k_select function makes 
        on a list of 1000 integers.
        """
        test_data = list(range(1000))
        random.shuffle(test_data)
        _, comparisons = top_k_select(test_data, 40)
        self.assertLess(comparisons, 40000)
        self.assertGreater(comparisons, 30000)

    def test_top_k_heap(self):
        """Tests the top_k_heap function on a list of 1000 integers."""
        test_data = list(range(1000))
        random.shuffle(test_data)
        top_40, _ = top_k_heap(test_data, 40)
        self.assertEqual(top_40, list(range(999, 959, -1)))

    def test_top_k_heap_comparisons(self):
        """Tests the number of comparisons made by the top_k_heap function 
        on a list of 1000 integers.
        """
        test_data = list(range(1000))
        random.shuffle(test_data)
        _, comparisons = top_k_heap(test_data, 40)
        self.assertLess(comparisons, 10400)
        self.assertGreater(comparisons, 1040)

class TestFastPriorityQueue(unittest.TestCase):
    """Tests for Task 2 on fast heapify."""

    def test_heapify(self):
        """Tests that heapify works on a small test case in sorted order."""
        fpq = FastPriorityQueue(list(range(10)))
        self.assertEqual(len(fpq), 10)
        self.assertEqual(fpq.validate(), True)

    def test_heapify_random_data(self):
        """Tests that heapify works on a small test case in random order."""
        test_data = list(range(1000))
        random.shuffle(test_data)
        fpq = FastPriorityQueue(test_data)
        self.assertEqual(len(fpq), 1000)
        self.assertEqual(fpq.validate(), True)

    # Your tests for testing the number of comparisons should go here if
    # you choose to use the unit testing framework (not this is not marked
    # and it is completely up to you on how you test your code).


class TestChangePriorityQueue(unittest.TestCase):
    """Tests for Task 3 on removing from a priority queue."""

    def test_heapify(self):
        """Tests that heapify still works correctly. Note this effectively
        tests whether swap items is swapping the items correctly and that
        the __init__ function has not been modified.
        """
        test_data = [str(digit) for digit in range(1000)]
        test_priorities = list(range(1000))
        random.shuffle(test_priorities)
        cpq = ChangePriorityQueue(test_data, test_priorities)
        self.assertEqual(len(cpq), 1000)
        self.assertEqual(cpq.validate(), True)

    def test_insert_with_priority(self):
        """Tests the insert_with_priority method on a small example."""
        cpq = ChangePriorityQueue()
        cpq.insert_with_priority('a', 1)
        cpq.insert_with_priority('b', 3)
        cpq.insert_with_priority('c', 8)
        cpq.insert_with_priority('d', 0)
        cpq.insert_with_priority('e', 4)
        self.assertEqual(len(cpq), 5)
        self.assertEqual(cpq.validate(), True)

    def test_peek_max(self):
        """Tests the peek_max method on a small example."""
        cpq = ChangePriorityQueue()
        cpq.insert_with_priority('a', 1)
        cpq.insert_with_priority('b', 3)
        cpq.insert_with_priority('c', 8)
        cpq.insert_with_priority('d', 0)
        cpq.insert_with_priority('e', 4)
        self.assertEqual(cpq.peek_max(), 'c')

    def test_pop_max(self):
        """Tests the pop_max method on a small 7 item example."""
        test_priorities = [3, 67, 65, 8, 412, 1, 22]
        test_data = list(string.ascii_lowercase)[:len(test_priorities)]
        cpq = ChangePriorityQueue(test_data, test_priorities)
        self.assertEqual(len(cpq), 7)
        self.assertEqual(cpq._item_indices['g'], 6)
        self.assertEqual(cpq.pop_max(), 'e')
        self.assertEqual(len(cpq), 6)
        self.assertEqual(cpq._item_indices['g'], 1)
        self.assertEqual(cpq.validate(), True)

    def test_remove_item(self):
        """Tests the remove_item method on a small 7 item example."""
        test_priorities = [3, 67, 65, 8, 412, 1, 22]
        test_data = list(string.ascii_lowercase)[:len(test_priorities)]
        cpq = ChangePriorityQueue(test_data, test_priorities)
        self.assertEqual(len(cpq), 7)
        self.assertEqual(cpq.pop_max(), 'e')
        self.assertEqual(len(cpq), 6)
        self.assertEqual(cpq.remove_item('g'), 'g')
        self.assertEqual(cpq.remove_item('g'), None) # pq no longer contains 'g'
        self.assertEqual(cpq.remove_item(3), None)
        self.assertEqual(cpq.validate(), True)
        self.assertEqual(len(cpq), 5)
        self.assertEqual(cpq.pop_max(), 'b')
        self.assertEqual(cpq.pop_max(), 'c')
        self.assertEqual(cpq.remove_item('d'), 'd')
        self.assertEqual(cpq.remove_item('d'), None)
        self.assertEqual(len(cpq._item_indices), 2)
        self.assertEqual(cpq._item_indices['a'], 0)
        self.assertEqual(cpq._item_indices['f'], 1)
        self.assertEqual(cpq.validate(), True)

class TestDheapPriorityQueue(unittest.TestCase):
    """Tests for Task 4 on d-heaps."""

    def test_parent_index(self):
        """Tests whether the correct parent index is found with d=5."""
        dpq = DheapPriorityQueue(list(range(100)), 5)
        self.assertEqual(dpq._parent_index(6), 1)
        self.assertEqual(dpq._parent_index(10), 1)
        self.assertEqual(dpq._parent_index(30), 5)
        self.assertEqual(dpq._parent_index(0), -1)
        self.assertEqual(dpq._parent_index(100), -1) # 100 is not in the d-heap.

    def test_children_indices(self):
        """Tests whether the correct children indices are found with d=7."""
        dpq = DheapPriorityQueue(list(range(100)), 7)
        self.assertEqual(sorted(dpq._children_indices(0)), list(range(1, 8)))
        self.assertEqual(sorted(dpq._children_indices(10)), list(range(71, 78)))

    def test_heapify(self):
        """Tests whether heapify still works correctly in a large case with d=7."""
        dpq = DheapPriorityQueue(list(range(10000)), 7)
        self.assertEqual(len(dpq), 10000)
        self.assertEqual(dpq.validate(), True)

    def test_insert(self):
        """Tests whether heapify still works correctly in a large case with d=7."""
        dpq = DheapPriorityQueue(branch_factor=6)
        dpq.insert(5)
        dpq.insert(4)
        dpq.insert(6)
        dpq.insert(3)
        dpq.insert(2)
        dpq.insert(7)
        self.assertEqual(len(dpq), 6)
        self.assertEqual(dpq.validate(), True)

    def test_pop_max_small(self):
        """Tests whether pop_max still works correctly in a small case with d=3."""
        dpq = DheapPriorityQueue([3, 67, 65, 8, 412, 1, 22], 3)
        self.assertEqual(len(dpq), 7)
        self.assertEqual(dpq.pop_max(), 412)
        self.assertEqual(len(dpq), 6)
        self.assertEqual(dpq.validate(), True)

    def test_pop_max_big(self):
        """Tests whether pop_max still works correctly in a big case with d=13."""
        dpq = DheapPriorityQueue(list(range(10000)), 13)
        for item in range(9999, 8000, -1):
            self.assertEqual(dpq.pop_max(), item)
        self.assertEqual(len(dpq), 8001)
        self.assertEqual(dpq.validate(), True)


def all_tests_suite():
    """Returns a unit_test suite containing all desired tests."""
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestTopK))
    # uncomment the next lines when ready to rumble with those tests
    suite.addTest(unittest.makeSuite(TestFastPriorityQueue))
    suite.addTest(unittest.makeSuite(TestChangePriorityQueue))
    suite.addTest(unittest.makeSuite(TestDheapPriorityQueue))
    return suite

def main():
    """Runs all tests returned by all_tests_suite()."""
    test_runner = unittest.TextTestRunner(verbosity=0)
    test_runner.run(all_tests_suite())

if __name__ == '__main__':
    main()