from quicksort import *

def common_items(list_x,list_y):
    """Returns a list containing all the items in x that are also in y.
    The resulting list should be in order.
    Clashes need only be listed once.
    Returns an empty list if there are none.
    >>> common_items([0,1,2,3],[0,0,2,4])
    [0, 2]
    >>> common_items([0,1,2,3],[1,2,3,4])
    [1, 2, 3]
    >>> common_items([0,1,2,3],[3,2,1,0])
    [0, 1, 2, 3]
    >>> common_items([0,1,2,3],[5,6,7,8])
    []
    >>> common_items([],[5,6,7,8])
    []
    >>> common_items([1,2,3,4],[])
    []
    >>> common_items([],[])
    []
    
    """

    #Your code goes here
    #You should have just finished a nice sort function you can use
    #to sort the lists in to order
    common = []
    pos1 = 0
    pos2 = 0
    x = len(list_x)
    y = len(list_y)
    a = quicksort(list_x, style='Mo3-pivot')
    b = quicksort(list_y, style='Mo3-pivot')  
    count = 0
    if x < 1 or y < 1:
        return common
    while pos1 < x and pos2 < y:
        first = b[pos1]
        second = a[pos2]   
        count += 1
        if first == second:
            common.append(second)             
            pos1 += 1
            pos2 += 1              
        else:
            count += 1
            if first < second:
                pos1 += 1
            else:
                pos2 += 1    
    return common, count

if __name__ == "__main__": 
    doctest.testmod()
