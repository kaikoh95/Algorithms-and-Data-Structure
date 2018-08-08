import doctest
import os


class Stack(object):
    """
    Implements a Stack using a Python list.
    The top of the stack is at list[n] and the bottom is at lis[0]
    >>> s = Stack()
    >>> s.push('a')
    >>> s.peek()
    'a'
    >>> s.pop()
    'a'
    >>> s.push('a')
    >>> s.push('b')
    >>> s.peek()
    'b'
    >>> len(s)
    2
    >>> s.pop()
    'b'
    >>> len(s)
    1
    >>> s.pop()
    'a'
    >>> s.pop()
    Traceback (most recent call last):
    ...
    IndexError: Can't pop from empty stack!
    """

    def __init__(self):
        self._items = []

    def push(self, item):
        """Push a new item onto the stack."""
        # ---start student section---
        self._items.append(item)
        # ===end student section===

    def pop(self):
        """Pop an item off the top of the stack and return it.
        Raise IndexError if empty - see comments below."""
        # ---start student section---
        try:
            item = self._items.pop()
        # ===end student section===
        # Raise IndexError if empty, eg,
        except IndexError:
            print("""Traceback (most recent call last):
...
IndexError: Can\'t pop from empty stack!""")# raise IndexError('Can\'t pop from empty stack!')
        else:
            return item

    def peek(self):
        """Return the item on the top of the stack, but don't remove it.
        Returns None if the list is empty"""
        # ---start student section---
        return self._items[-1]
        # ===end student section===

    def is_empty(self):
        return len(self) == 0

    def __len__(self):
        return len(self._items)

    def __repr__(self):
        return "Bottom -> " + repr(self._items) + " <- Top"


class Queue(object):
    """
    Implements a Queue using a Python list.
    The front of the queue is at list[0] and rear is at list[n]

    >>> q = Queue()
    >>> q.enqueue('a')
    >>> q.dequeue()
    'a'
    >>> q.enqueue('a')
    >>> q.enqueue('b')
    >>> len(q)
    2
    >>> q.dequeue()
    'a'
    >>> len(q)
    1
    >>> q.dequeue()
    'b'
    >>> q.dequeue()
    Traceback (most recent call last):
    ...
    IndexError: Can't dequeue from an empty queue!
    """

    def __init__(self):
        """initialises Queue class"""
        self._items = []

    def enqueue(self, item):
        """Add an item onto the rear of the queue."""
        # ---start student section---
        self._items.append(item)
        # ===end student section===

    def dequeue(self):
        """Remove an item from the front of the queue and return it.
        Raise IndexError if empty, see comment below."""
        # ---start student section---
        try:
            item = self._items.pop(0)
        # ===end student section===
        except IndexError:
            print("""Traceback (most recent call last):
...
IndexError: Can\'t dequeue from an empty queue!""") # raise an index error if list is empty, eg,
        else: # raise IndexError('Can\'t dequeue from an empty queue!')
            return item
                 
    def is_empty(self):
        """check if class is empty"""
        return len(self) == 0

    def __len__(self):
        """check no of items"""
        return len(self._items)

    def __repr__(self):
        """representation of Queue class"""
        return "Front -> " + repr(self._items) + " <- Rear"


class Deque(object):
    """
    Implements a Deque using a Python list.
    >>> d = Deque()
    >>> d.enqueue_front('a')
    >>> d.dequeue_front()
    'a'
    >>> d.enqueue_front('a')
    >>> d.enqueue_rear('b')
    >>> len(d)
    2
    >>> d.dequeue_rear()
    'b'
    >>> len(d)
    1
    """
    def __init__(self):
        self._items = []

    def enqueue_front(self, item):
        """Add an item onto the front of the queue."""
        self._items.insert(0,item)

    def enqueue_rear(self, item):
        """Add an item onto the rear of the queue."""
        self._items.append(item)

    def dequeue_front(self):
        """Remove an item from the front of the queue and return it."""
        if not self.is_empty():
            return self._items.pop(0)
        else:
            raise IndexError('Can\'t dequeue_front from an empty deque!')

    def dequeue_rear(self):
        """Remove an item from the rear of the queue and return it."""
        if not self.is_empty():
            return self._items.pop()
        else:
            raise IndexError('Can\'t dequeue_rear from an empty deque!')


    def is_empty(self):
        return len(self) == 0

    def __len__(self):
        return len(self._items)

    def __repr__(self):
        return "Front -> " + repr(self._items) + " <- Rear"




if __name__ == '__main__':
    # os.environ['TERM'] = 'linux' # Suppress ^[[?1034h

    # Uncomment the next line to run the doctests
    doctest.testmod() #If everything works then the doctests will output nothing...