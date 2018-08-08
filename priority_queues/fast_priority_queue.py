"""Module containing a priority queue implemented as a binary heap with a
fast heapify method.
"""
from basic_priority_queue import BasicPriorityQueue

class FastPriorityQueue(BasicPriorityQueue):
    """Implementation of a binary max-heap based priority queue fast heapify."""   

    def _heapify(self):
        """Converts the list to heap order. On average it uses
        considerably fewer comparisons than inserting each item
        individually.
        """      
        size = len(self._items)
        for index in range((size // 2) - 1, -1, -1):
            self._sift_down(index)