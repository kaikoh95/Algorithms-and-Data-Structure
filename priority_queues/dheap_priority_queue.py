"""Module containing a priority queue implemented as a max-heap with a given
branch factor d, where d >= 2.
"""
from basic_priority_queue import BasicPriorityQueue

class DheapPriorityQueue(BasicPriorityQueue):
    """Implementation of a max-heap based priority queue with a specified
    heap branch factor.
    """

    def __init__(self, initial_items=None, branch_factor=2):
        """Makes a new priority queue containing initial_items and uses
        branch_factor as the branching factor (i.e. d) for the underlying
        d-heap. The branch factor is two or greater.
        """
        self._branch_factor = branch_factor
        super().__init__(initial_items)

    def _parent_index(self, index):
        """Returns the index of the parent of the given index or -1 if the
        index has no parent (i.e., is root or not even in the list). Note the
        list items is 0-indexed, i.e., the root _item is at position 0.
        """
        
        parent = (index - 1) // self._branch_factor
        if 0 < index < len(self):
            return parent
        return -1

    def _children_indices(self, index):
        """Returns a list of the indices of the children of the given
        index. Any child index larger than or equal to the number of
        items is omitted. This results in an empty list being returned
        in the case where the item is a leaf (has no children) in
        the d-heap. The empty list should be returned if index is out
        of bounds of _items. Note the list _items is 0-indexed, i.e. the
        root item is at position 0.
        """
        
        children = []
        if index >= len(self):
            return children
        for i in range(1, self._branch_factor + 1):
            child = index * self._branch_factor + i
            if child < (len(self)):
                children.append(child)
            else:
                break
        return children