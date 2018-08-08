def load_file(file_name):
    data_list = []
    v = 0
    f = open(file_name)
    line = f.readline()
    while line != "":
        line.strip()
        line = int(line)
        data_list = data_list + [line]
        line = f.readline()
    return data_list

    
        
def selection_sort(file_name):
    alist = load_file(file_name)
    n_comps = 0
    count = 0
    for fillslot in range(len(alist)-1, 0, -1):
        positionOfMax  = 0
        for location in range(1, fillslot+1):
            n_comps += 1
            if alist[location] > alist[positionOfMax]:
                positionOfMax = location
        alist[fillslot], alist[positionOfMax]  = alist[positionOfMax], alist[fillslot] 
        count += 1
    print("Selection sort on {0}, {1:d} items, used {2:d} comparisons, {3} swaps".
          format(file_name,len(alist),n_comps, count))
    return alist




def insertion_sort(alist):
    #alist = load_file(file_name)
    count = 0
    for index in range(1, len(alist)):
        stop = False
        currentvalue = alist[index]
        print(currentvalue)
        position = index
        print(position)
        print()
        while position > 0 and not(stop):
            if alist[position-1] > currentvalue:
                count += 1
                alist[position] = alist[position-1]
                print(alist[position])
                print(alist[position-1])
                position = position - 1
                print(position)
            else:
                stop = True
        print()
        alist[position] = currentvalue
        print(alist[position])
    return 'count: {}, length:{}, list:{}'.format(count, len(alist), alist)



        
def gap_insertion_sort(alist, start, gap):
    """In-place insertion sort on alist with given start and gap."""
    count = 0
    for i in range (start+gap, len(alist), gap):
        currentvalue = alist[i]
        position = i
        stop = False
        while position >= gap and not(stop):
            count += 1
            if alist[position-gap] > currentvalue:
                alist[position] = alist[position - gap]
                position = position - gap
            else:
                stop = True
        alist[position] = currentvalue
    return count
        




def shell_sort(file_name):
    alist = load_file(file_name)
    sublistcount = len(alist) // 2
    gaplist = []
    n_comps = 0
    while sublistcount > 0 :
        for startposition in range(sublistcount):
            count = gap_insertion_sort(alist, startposition, sublistcount)
            n_comps += count
        gaplist.append(sublistcount)
        sublistcount = sublistcount // 2      
    print("Shell sort on {0}, {1:d} items, used {2:d} comparisons. Gaps were {3}".format(file_name,len(alist),n_comps, str(gaplist)))
    return alist
    



def shell_sort2(file_name, gaplist):
    # ---start student section---
    alist = load_file(file_name)
    n_comps = 0
    for i in range(len(gaplist)):
        sublistcount = gaplist[i]
        for startposition in range(sublistcount):
            count = gap_insertion_sort(alist, startposition, sublistcount)
            n_comps += count    
    print("Shell sort on {0}, {1:d} items, used {2:d} comparisons. Gaps were {3}".format(file_name,len(alist),n_comps, str(gaplist)))
    return alist
    # ===end student section===



