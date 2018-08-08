"""Module containing a priority queue that can remove arbitrary items."""
from basic_priority_queue import BasicPriorityQueue

class ChangePriorityQueue(BasicPriorityQueue):
    """Implementation of a binary max-heap based priority queue with remove
    item functionality.
    """

    def __init__(self, initial_items=None, initial_priorities=None):
        """Makes a new priority queue containing initial_items and uses
        the corresponding position in initial_priorities as the priority
        for each item.
        """
        if initial_items is not None and initial_priorities is not None:
            initial_indices = range(len(initial_items))
            self._item_indices = dict(zip(initial_items, initial_indices))
            items = list(zip(initial_priorities, initial_items))
            super().__init__(items)
        else:
            self._item_indices = dict()
            super().__init__()

    def insert(self, item):
        """Insert cannot be used in change_priority_queue as the priority must
        be explicitly given.
        """
        raise TypeError("Also need priority. Call insert_with_priority instead!")

    def _swap_items(self, index, swap_index):
        """Swaps the items at the given indices in the heap and updates
        the _item_indices dictionary to be consistent with the change.
        """
        
        indices = self._item_indices
        items = self._items
        priority1, item1 = items[index]
        priority2, item2 = items[swap_index] 
        items[index] = priority2, item2
        items[swap_index] = priority1, item1
        indices[item1], indices[item2] = indices[item2], indices[item1]
        
            
    def insert_with_priority(self, item, priority):
        """Inserts a given item into the heap with the given priority. Updates
        the _item_indices dictionary to be consistent with the insert.
        """
        
        to_insert = (priority, item)
        self._items.append(to_insert)
        if len(self) == 0:
            self._item_indices[item] = 0
        else:
            self._item_indices[item] = len(self) - 1
            self._sift_up(len(self) - 1)
        
        
    def peek_max(self):
        """Returns the largest item in the heap."""
        
        _, item = self._items[0]
        return item
        

    def pop_max(self):
        """Removes the largest item in the heap and returns it. Returns None if
        there are no items in the heap. Can be thought of as popping the max
        item off the heap. Updates the _item_indices dictionary to be
        consistent with the removal."""
        
        if len(self) == 0:
            return None
        else:
            _, item = self._items[0]
            self._item_indices.pop(item)
            last_priority, last_item = self._items.pop()
            if len(self) > 0:
                self._items[0] = (last_priority, last_item)
                self._item_indices[last_item] = 0
                self._sift_down(0)                
            return item


    def remove_item(self, item):
        """Removes and returns a specific item from the priority queue.
        If the item is not in the priority queue this method does nothing
        and returns None. in the case of removal this method Updates the
        _item_indices dictionary to be consistent with the removal.
        """
        
        if item not in self._item_indices:
            return None
        else:
            index = self._item_indices[item]
            if index == len(self) - 1:
                self._items.pop()
                self._item_indices.pop(item)
            else:
                priority, last_item = self._items.pop()
                self._items[index] = (priority, last_item)
                self._item_indices[last_item] = index
                self._item_indices.pop(item)
                parent = (index - 1) // 2
                priority_i, _ = self._items[index]                
                priority_p, _ = self._items[parent]
                if priority_i > priority_p:
                    self._sift_up(index)
                else:    
                    self._sift_down(index)
            return item
        
q=ChangePriorityQueue()
q.insert_with_priority('a',10)


print(q.remove_item('a'))
print(q, q._item_indices)

my_pq = ChangePriorityQueue()
my_pq.insert_with_priority('a', 5)
my_pq.insert_with_priority('b', 2)
my_pq.insert_with_priority('c', 7)
my_pq.insert_with_priority('d', 3)
print(my_pq)
print(my_pq._item_indices) #note print order is random for dict.
print(my_pq.remove_item('d'))
print(my_pq)
print(my_pq._item_indices) #note print order is random for dict.
print(my_pq.remove_item('b'))
print(my_pq)
print(my_pq._item_indices)
print(my_pq.remove_item('b'))
print(my_pq)
print(my_pq._item_indices) #note print order is random for dict.
print(my_pq.pop_max())
print(my_pq._item_indices)