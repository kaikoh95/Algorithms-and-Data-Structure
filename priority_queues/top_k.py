"""Module containing some methods for finding the largest k
items in a list.
"""
from basic_priority_queue import BasicPriorityQueue

def top_k_select(items, k):
    """Uses a modified max-selection sort to find the max k items of a list.
    This sort terminates once the max k values are found. Note that
    this function does not modify the list items. This function returns
    a descending list of the top k items and the number of item comparisons
    made.
    """
    alist = list(items) # Makes a copy of items.
    top_k = []
    n_comps = 0
    for fillslot in range(len(alist)-1, 0, -1):
        position_max = 0
        if len(top_k) < k:
            for location in range(1, fillslot+1):
                n_comps += 1
                if alist[location] > alist[position_max]:
                    position_max = location
                alist[fillslot], alist[position_max] = alist[position_max], alist[fillslot]
            top_k.append(alist[fillslot])
        else:
            break
    return top_k, n_comps



def top_k_heap(items, k):
    """Uses a BasicPriorityQueue to find the max k items of a list. Note this
    function does not modify the list items. This function returns
    a descending list of the top k items and the number of item comparisons
    made.
    """
    alist = list(items) # Makes a copy of items.
    basic = BasicPriorityQueue(alist)
    result = []
    n_comps = 0
    index = 0
    while index < k:
        alpha = basic.pop_max()
        result.append(alpha)
        index += 1
    n_comps = basic.get_comparisons()
    return result, n_comps