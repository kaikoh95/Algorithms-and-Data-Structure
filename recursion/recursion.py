from random import *
from turtle import *

COUNT = 0

class Node:
    def __init__(self,item):
        self.data = item
        self.next_node = None

        
def add_item_to_list(first_node, item):
    """
    Adds item to end of linked list.
    first_node is the first node in the list.
    """
    if first_node == None:
        # the list needs a first node
        # initialise a first node with first_node = Node(item)
        # then call add_item_to_list to add another node
        raise IndexError ("None doesn't have a .next")
    else:
        new_node = Node(item)
        current_node = first_node
        #traverse list until at last node
        while current_node.next_node != None:
            current_node = current_node.next_node
        #set last node's next pointer to point to the new node
        current_node.next_node = new_node

            
 
def power(x, n):
    """Computes x**n"""
    if n == 0:
        ans = 1
        count = 0
    else:
        po, count = power(x, n-1)
        ans = x * po
        count += 1
    return ans, count
    
    
                         
                         

def gcd(a,b):
    """Computes the greatest common divisor of a and b."""
    if b == 0:
        return a
    elif a < b:
        return gcd(b, a)
    else:
        return gcd(a-b, b)

    
def str_length(s):
    """
    Calculates the length of a string.
    Definitely not the best way of doing this!
    Think about how much space all the sub lists will take up.
    """
    if s == "":
        return 0
    return 1 + str_length(s[1:])
    

def fib_recursive(n):
    """Returns the 'n'th Fibonacci number.
    >>> fib_recursive(0)
    0
    >>> fib_recursive(1)
    1
    >>> fib_recursive(2)
    1
    >>> fib_recursive(3)
    2
    >>> fib_recursive(4)
    3
    >>> fib_recursive(9)
    34
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_recursive(n-1)+fib_recursive(n-2)
    
    

def fib_iterative(n):
    """Returns the 'n'th Fibonacci number.
    >>> fib_iterative(0)
    0
    >>> fib_iterative(1)
    1
    >>> fib_iterative(2)
    1
    >>> fib_iterative(3)
    2
    >>> fib_iterative(4)
    3
    >>> fib_iterative(9)
    34
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        fib_n_minus2 = 0
        fib_n_minus1 = 1      # start with fib of 2 which equals 1
        for i in range(1,n):  # there will be n+1 numbers including the 0'th
            curr_fib = fib_n_minus1 + fib_n_minus2
            fib_n_minus2 = fib_n_minus1
            fib_n_minus1 = curr_fib
        return curr_fib



def fibonacci_sequence(n):
    """
    Prints Fibonacci numbers up to the nth number (including the 0th number).

    >>> fibonacci_sequence(9)
    0 1 1 2 3 5 8 13 21 34
    """
    if n == 0:
        print(0, end='')
    else:
        fibonacci_sequence(n-1)
        print(' ' + str(fib_recursive(n)), end='')


    
def tree(size,level):
    """
     Draws a funky fractal tree.
     Feel free to experiment with parameters...
     """    
    if level!=0:
        forward(random()*size)
        x = pos()
        angle=random()*20
        right(angle)
        tree(size*.8,level-1)
        setpos(x)
        left(angle)
        angle=random()*-20
        right(angle)
        tree(size*.8,level-1)
        left(angle)
        setpos(x)



#-------------------------------------------------------------------------------
#Functions for students to implement
#-------------------------------------------------------------------------------
        
def linked_list_length(list_node):
    """
    Returns the number of nodes in a linked list,
    0 if list is empty.
    
    >>> first_node = Node(1)
    >>> linked_list_length(first_node)
    1
    >>> add_item_to_list(first_node, 2)
    >>> linked_list_length(first_node)
    2
    >>> add_item_to_list(first_node, 3)
    >>> linked_list_length(first_node)
    3
    >>> add_item_to_list(first_node, 4)
    >>> linked_list_length(first_node)
    4
    >>> add_item_to_list(first_node, 10)
    >>> linked_list_length(first_node)
    5
    """
    # ---start student section---
    if list_node is None:
        return 0
    else:
        return 1 + linked_list_length(list_node.next_node)
    # ===end student section===
    
    
def linked_list_print(list_node):
    """
    Prints list, one item per line.
    
    >>> first_node = Node(1)
    >>> linked_list_print(first_node)
    1
    >>> add_item_to_list(first_node, 2)
    >>> linked_list_print(first_node)
    1
    2
    >>> add_item_to_list(first_node, 3)
    >>> linked_list_print(first_node)
    1
    2
    3
    >>> add_item_to_list(first_node, 4)
    >>> linked_list_print(first_node)
    1
    2
    3
    4
    """
    # ---start student section---
    if list_node is None:
        pass
    else:
        print(list_node.data)
        linked_list_print(list_node.next_node)
    # ===end student section===
    

def linked_list_reverse_print(list_node):
    """
    Prints list in reverse, one item per line.
    
    >>> first_node = Node(1)
    >>> linked_list_reverse_print(first_node)
    1
    >>> add_item_to_list(first_node, 2)
    >>> linked_list_reverse_print(first_node)
    2
    1
    >>> add_item_to_list(first_node, 3)
    >>> linked_list_reverse_print(first_node)
    3
    2
    1
    >>> add_item_to_list(first_node, 4)
    >>> linked_list_reverse_print(first_node)
    4
    3
    2
    1
    """
    # ---start student section---
    if list_node is None:
        pass
    else:
        linked_list_reverse_print(list_node.next_node)
        print(list_node.data)
    # ===end student section===
    
   
def is_in_linked_list(list_node,item):
    """
    Returns TRUE if item is in list, otherwise False.
    
    >>> first_node = Node(1)
    >>> is_in_linked_list(first_node,2)
    False
    >>> add_item_to_list(first_node, 2)
    >>> is_in_linked_list(first_node,2)
    True
    >>> add_item_to_list(first_node, 3)
    >>> add_item_to_list(first_node, 4)
    >>> add_item_to_list(first_node, 5)
    >>> is_in_linked_list(first_node,3)
    True
    >>> is_in_linked_list(first_node,10)
    False
    """
    # ---start student section---
    if list_node is None:
        return False
    elif list_node.data == item:
        return True
    else:
        return is_in_linked_list(list_node.next_node, item)
        
    # ===end student section===

        
        

def factorial(n):
    """Returns n!
    >>> factorial(0)
    1
    >>> factorial(1)
    1
    >>> factorial(5)
    120
    """
    # ---start student section---
    if n == 0 or n == 1:
        return 1
    else:
        return factorial(n - 1) * n
    # ===end student section===


    
def quick_power(x,n):
    """
    Computes x ^ n where n is an integer
    NOTE: You need to write the doc test for the base case.
    >>> quick_power(2, 0)
    1
    >>> quick_power(2,3)
    8
    >>> quick_power(2,8)
    256
    >>> quick_power(2,16)
    65536
    
    """
    # ---start student section---
    if n == 0:
        ans = 1
        count = 0
    elif n % 2 == 0:
        qphalf, count = quick_power(x, n / 2)
        ans = qphalf * qphalf
        count += 1
    else:
        qp, count = quick_power(x, n - 1)
        ans = qp * x
        count += 1
    return ans, count
    # ===end student section===

    
    
def recursive_string_print(s):
    """
    Prints a string out, one character per line, using recursion
    Think about why this is very inefficient for long strings
    >>> recursive_string_print('string')
    s
    t
    r
    i
    n
    g
    """
    # ---start student section---
    if len(s) > 0:
        print(s[0])
        recursive_string_print(s[1:])
    # ===end student section===



def recursive_reverse_string_print(s):
    """
    Prints a string out in reverse, one character per line, using recursion
    Think about why this is very inefficient for long strings!
    >>> recursive_reverse_string_print('string')
    g
    n
    i
    r
    t
    s
    """
    # ---start student section---
    if len(s) > 0:
        print(s[-1])
        recursive_reverse_string_print(s[:-1])
    # ===end student section===

    
    

if __name__ == '__main__':
    import doctest
    import os
    os.environ['TERM'] = 'linux' # Suppress ^[[?1034h
    # Uncomment next line to run the tests
    doctest.testmod()  # sc
    
    #n = 5000
    #print('fib({0:d}) = {1:d}'.format(n,fib_iterative(n)))
    #print('\n')
    
    #n = 100
    #print('fib({0:d}) = {1:d}'.format(n,fib_iterative(n)))
    #print('\n')
    
    #n = 31
    #print('fib({0:d}) = {1:d}'.format(n,fib_recursive(n)))
    #print('\n')

    #Given the value for fib_iterative(100) would it be wise 
    #to try to run fib_recursive(100)????
    
    
    #my_list=Node('b')
    #add_item_to_list(my_list,'a')
    #linked_list_print(my_list)
    