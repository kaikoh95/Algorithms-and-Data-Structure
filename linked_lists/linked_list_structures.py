'''Data structures implemented with linked lists.'''
import doctest
import os



class Node:
    '''A node for a linked list.'''

    def __init__(self, initdata):
        self.data = initdata
        self.next_node = None


class Stack(object):
    """ Implements a Stack using a Linked List"
    >>> s = Stack()
    >>> print(s)
    List for stack is: None
    >>> result = s.pop()
    Traceback (most recent call last):
    ...
    IndexError: Can't pop from empty stack.
    >>> s.push('a')
    >>> print(s)
    List for stack is: a -> None
    >>> len(s)
    1
    >>> s.pop()
    'a'
    >>> print(s)
    List for stack is: None
    >>> s.push('b')
    >>> print(s)
    List for stack is: b -> None
    >>> s.push('c')
    >>> print(s)
    List for stack is: c -> b -> None
    >>> len(s)
    2
    >>> s.peek()
    'c'
    >>> print(s)
    List for stack is: c -> b -> None
    >>> s.pop()
    'c'
    >>> print(s)
    List for stack is: b -> None
    >>> e = Stack()
    >>> e.peek()
    Traceback (most recent call last):
    ...
    IndexError: Can't peek at empty stack.
    """

    def __init__(self):
        self.head = None

    def push(self, item):
        """push a new item on to the stack"""
        # ---start student section---
        temp = Node(item)
        temp.next_node = self.head
        self.head = temp
        # ===end student section===

    def pop(self):
        """pop an item off the top of the stack, and return it
        If stack is empty you should raise an IndexError as per
        the comment below."""
        # use the following line to raise error when stack is empty
        # raise IndexError("Can't pop from empty stack.")
        # ---start student section---
        if self.is_empty():
            raise IndexError("Can't pop from empty stack.")
        else:
            temp = self.head.data
            self.head = self.head.next_node
            return temp
        # ===end student section===

    def peek(self):
        """pop an item on the top of the top of the stack, but don't remove it.
        If stack is empty you should raise an IndexError as per
        the comment below.
        """
        # use the following line to raise error when stack is empty
        # raise IndexError("Can't peek at empty stack.")
        # ---start student section---
        if self.is_empty():
            raise IndexError("Can't peek at empty stack.")
        else:
            return self.head.data
        # ===end student section===

    def is_empty(self):
        """ Returns True if stack is empty """
        return self.head is None

    def __len__(self):
        """ Returns the length --- calling len(s) will invoke this method """
        # ---start student section---
        count = 0
        alpha = self.head
        while alpha is not None:
            count += 1
            alpha = alpha.next_node
        return count
        # ===end student section===

    def __str__(self):
        """Returns a string representation of the list for the stack starting
        from the beginning of the list. Items are separated by ->
        and ending with -> None
        See doctests in class docstring
        """
        # ---start student section---
        string = 'List for stack is: '
        alpha = self.head
        while alpha is not None:
            string += alpha.data
            string += ' -> '
            alpha = alpha.next_node
        if alpha is None:
            string += 'None'
        return string                
        # ===end student section===


class Queue(object):
    """ Implements a Queue using a Linked List"
    >>> q = Queue()
    >>> len(q)
    0
    >>> print(q)
    List for queue is: None
    >>> result = q.dequeue()
    Traceback (most recent call last):
    ...
    IndexError: Can't dequeue from empty queue.
    >>> q.enqueue('a')
    >>> print(q)
    List for queue is: a -> None
    >>> len(q)
    1
    >>> q.dequeue()
    'a'
    >>> len(q)
    0
    >>> q.enqueue('a')
    >>> q.enqueue('b')
    >>> print(q)
    List for queue is: a -> b -> None
    >>> q.enqueue('c')
    >>> print(q)
    List for queue is: a -> b -> c -> None
    >>> len(q)
    3
    >>> q.dequeue()
    'a'
    >>> print(q)
    List for queue is: b -> c -> None
    """

    def __init__(self):
        self.head = None

    def enqueue(self, item):
        """Add an item onto the tail of the queue."""
        # ---start student section---
        new = Node(item)
        new.next_node = None
        if self.head is None:
            self.head = new
        else:
            alpha = self.head
            while self.head.next_node is not None:
                self.head = self.head.next_node
            if self.head.next_node is None:
                self.head.next_node = new
                self.head = alpha
        # ===end student section===

    def dequeue(self):
        """Remove an item from the head of the queue and return it.
        If queue is empty you should raise an IndexError as per
        the comment below."""
        # use the following line to raise error when queue is empty
        # raise IndexError("Can't dequeue from empty queue.")
        # ---start student section---
        if self.is_empty():
            raise IndexError("Can't dequeue from empty queue.")
        else:
            temp = self.head.data
            self.head = self.head.next_node
            return temp
        # ===end student section===

    def is_empty(self):
        """ returns True if the queue is empty """
        # ---start student section---
        return self.head is None
        # ===end student section===

    def __len__(self):
        """ Returns the length --- calling len(q) will invoke this method """
        # ---start student section---
        count = 0
        alpha = self.head
        while alpha is not None:
            count += 1
            alpha = alpha.next_node
        return count
        # ===end student section===

    def __str__(self):
        """Returns a string representation of the list for the queue starting
        from the beginning of the list. Items are separated by ->
        and ending with -> None
        See doctests in class docstring
        """
        # ---start student section---
        string = 'List for queue is: '
        alpha = self.head
        while alpha is not None:
            string += alpha.data
            string += ' -> '
            alpha = alpha.next_node
        if alpha is None:
            string += 'None'
        return string           
        # ===end student section===


if __name__ == '__main__':
    os.environ['TERM'] = 'linux'  # Suppress ^[[?1034h
    # Uncomment the testmod() line to run the tests
    # Can enter an infinite loop if your Stack isn't implemented correctly
    doctest.testmod()
