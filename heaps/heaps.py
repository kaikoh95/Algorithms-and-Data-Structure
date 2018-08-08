import doctest
import os


#--------------------------------------------------
def load_file(file_name):
    alist = []
    v = 0
    f = open(file_name)
    line = f.readline()
    while line != "":
        line.strip()
        line = int(line)
        alist = alist + [line]
        line = f.readline()
    return alist


#-------------------------------------------------
#-------------------------------------------------
class Heap(object):

    """An abstract interface for a Heap."""

    def __init__(self):
        # Create a list to store heap items.
        # First item is simply a spacer
        # Heap contents will start from index 1
        self._items = [0]

    def insert(self, item):
        # don't implement here
        # this is just a place holder
        pass

    def isEmpty(self):
        return len(self) == 0

    def __len__(self):
        """Returns the actual length of the heap,
        ie, how many items are in the heap
        Remember that item at index 0 is not part of the heap."""
        return len(self._items) - 1

    def __repr__(self):
        """Returns only the items in the heap,
        ie, leaves out _items[0] as the heap
        data starts from index 1..."""
        return repr(self._items[1:])


#-------------------------------------------------
#-------------------------------------------------
class MinHeap(Heap):

    """Implementation of a min-heap."""

    def __init__(self):
        super(MinHeap, self).__init__()

    #---------------------------------------------
    def insert(self, item):
        """Inserts a given item into the heap.

        >>> h = MinHeap()
        >>> h.insert(3)
        >>> h._items
        [0, 3]
        >>> h.insert(7)
        >>> h._items
        [0, 3, 7]
        >>> h.insert(5)
        >>> h._items
        [0, 3, 7, 5]
        >>> h.insert(2)
        >>> h._items
        [0, 2, 3, 5, 7]
        >>> h.insert(4)
        >>> h._items
        [0, 2, 3, 5, 7, 4]
        """
        
        self._items.append(item)
        self._sift_up(len(self._items) - 1)

    #-------------------------------------------------
    def _sift_up(self, index):
        """
        Moves the item at the given index up through the heap until it finds
        the correct place for it. That is, the item is moved up through the heap
        while it is smaller than its parent.
        """
        parent = (index) // 2
        # While we haven't reached the top of the heap, and its parent is
        # smaller than the item
        while index > 1 and self._items[index] < self._items[parent]:
            # Swap the item and its parent
            self._items[index], self._items[parent] = \
                self._items[parent], self._items[index]
            index = parent
            parent = (index) // 2

    #-------------------------------------------------
    def peek_min(self):
        """
        Returns the smallest item in the heap.

        >>> h = MinHeap()
        >>> h.insert(5)
        >>> h.validate()
        True
        >>> h.peek_min()
        5
        >>> h.insert(3)
        >>> h.peek_min()
        3
        >>> h.insert(7)
        >>> h.peek_min()
        3
        """
        return self._items[1]

    #-------------------------------------------------
    def pop_min(self):
        """
        Removes the smallest item in the heap and returns it. Returns None if
        there are no items in the heap. Can be thought of as Popping the min
        item off the heap.

        >>> h = MinHeap()
        >>> h.insert(5)
        >>> h.pop_min()
        5
        >>> len(h)
        0
        >>> h.insert(3)
        >>> h.insert(7)
        >>> h.pop_min()
        3
        >>> h.pop_min()
        7
        >>> len(h)
        0
        >>> tmp = list(map(h.insert, (3, 7, 5, 2, 4)))
        >>> print(h)
        [2, 3, 5, 7, 4]
        >>> h.pop_min()
        2
        >>> h._items[1]
        3
        >>> h._items[2]
        4
        >>> h.pop_min()
        3
        >>> h = MinHeap()
        >>> h.insert(1)
        >>> h.insert(5)
        >>> h.insert(2)
        >>> h.insert(7)
        >>> print(h)
        [1, 5, 2, 7]
        >>> h.validate()
        True
        >>> h.pop_min()
        1
        >>> print(h)
        [2, 5, 7]
        >>> h.validate()
        True
        """
        
        if len(self._items) == 0:
            return None
        else:
            value = self._items[1]
            self._items[1] = self._items[-1]
            self._items = self._items[:-1]
            self._sift_down(1)
            return value

    #-------------------------------------------------
    def _sift_down(self, index):
        """
        Moves an item at the given index down through the heap until it finds
        the correct place for it. That is, when the item is moved up through the
        heap while it is larger than either of its children.
        """
        # While the item at 'index' has at least one child...
        while (index * 2 + 1) <= len(self):
            left = 2 * index
            right = left + 1
            if self._items[left] > self._items[right]:
                smallest = right
            else:
                smallest = left
            if self._items[index] > self._items[smallest]:
                smallest_item = self._items[smallest]
                self._items[smallest] = self._items[index]
                self._items[index] = smallest_item
            else:
                # no need to go further as item smaller than smallest child
                break
            # Keep going down
            index = smallest

    #-------------------------------------------------
    def validate(self):
        """
        Validates the heap. Returns True if the heap is a valid min-heap, and
        False otherwise.

        >>> h = MinHeap()
        >>> h._items = [0, 1, 3, 5]
        >>> h.validate()
        True
        >>> h._items = [0, 1, 3, 5, 8, 9, 6, 7, 11]
        >>> h.validate()
        True
        >>> h._items = [0, 2, 3, 1, 7]
        >>> h.validate()
        False
        >>> h._items = [0, 5, 7, 2]
        >>> h.validate()
        False
        """

        valid = True
        i = 1
        left = i * 2 
        while left < len(self._items):
            if self._items[i] >= self._items[left]:
                valid = False
                return valid
            i += 1
            left = i * 2
        i = 1
        right = i * 2 + 1
        while right < len(self._items):
            if self._items[i] >= self._items[right]:
                valid = False
                return valid
            i += 1
            right = i * 2 + 1            
        return valid


if __name__ == '__main__':
    os.environ['TERM'] = 'linux'  # Suppress ^[[?1034h
    doctest.testmod()
    
    alist = load_file('list4.txt')
    h = MinHeap()
    for item in alist:
        h.insert(item)
    print(h)
    count = 1
    while count < 102:
        alpha = h.pop_min()
        print(count, ':', alpha)
        count += 1
