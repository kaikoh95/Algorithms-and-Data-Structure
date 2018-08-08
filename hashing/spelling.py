import re
import os
from time import clock
import doctest

    
def _c_mul(a, b):
    '''Substitute for c multiply function'''
    return ((int(a) * int(b)) & 0xFFFFFFFF)


def nice_hash(input_string):
    '''Takes a string name and returns a hash for the string. This hash value 
    will be os independent, unlike the default Python hash function.'''
    if input_string is None:
        return 0 # empty
    value = ord(input_string[0]) << 7
    for char in input_string:
        value = _c_mul(1000003, value) ^ ord(char)
    value = value ^ len(input_string)
    if value == -1:
        value = -2
    return value


def load_dict_words(filename):
    """
    Load a dictionary from a file, and returns a list of all words in the
    dictionary.
    Dictionary files should have one word per line.
    """
    with open(filename, 'r', encoding = 'latin-1') as file:
        words = [line.strip().lower() for line in file]
    return words

    
def load_doc_words(filename):
    """
    Loads a document from a file, and returns a list of all words in the
    document. 'Words' are sequences of one or more [A-Za-z] characters.
    Words are converted to lowercase.
    """
    with open(filename, 'r', encoding = 'ASCII') as file:
        words = [word.lower() for word in re.findall(r'[A-Za-z]+', file.read())]
    return words


    
#---------------------------------------------
# Start of Class definitions            
#---------------------------------------------
class ChainingHashTable():
    """A simple HashTable.
    ***** NOTE: These will fail initially, ie, when _hash returns 0
    ***** DON'T worry you will fix this later:)
    >>> hash_table = ChainingHashTable(5)
    >>> hash_table.store('George')
    >>> hash_table.store('Bungle')
    >>> hash_table.store('Zippy')
    >>> hash_table.store('Jane')
    >>> hash_table.store('Rod')
    >>> hash_table.store('Freddy')
    >>> print(hash_table)
    ChainingHashTable:
    slot        0 = ['Rod']
    slot        1 = ['George', 'Jane']
    slot        2 = ['Bungle']
    slot        3 = ['Zippy', 'Freddy']
    slot        4 = []
    n_slots = 5
    n_items in table = 6
    Load factor =  1.200
    <BLANKLINE>
    >>> print('Freddy' in hash_table)
    True
    >>> print('Dipsy' in hash_table)
    False
    """
        
    def __init__(self, slots=11):
        """
        Creates a new hashtable with a number of slots (default: 11).
        It will help if you always make your hash table size a prime number.
        
        Each slot will contain a list of items that hash to the slot.
        Initially the list in each slot contains a None.
        n_items contains the number of items that have been put in the table.
        """
        self._data = [[] for i in range(slots)]
        self.n_slots = slots
        self.n_items = 0
        
    def _hash(self, item):
        """Computes the hash of an item.
        First calculated the native python hash(item) and use modulo
        to reduce it down to a number in the range 0..slef.n_slots """
        
        #We will use a trivial hash function here to start with
        #Don't worry, you will get to update it later in the lab...
        index = nice_hash(item) % self.n_slots
        return index

    def store(self, item):
        """Appends an item to the list in the slot at _data[hash]."""
        index = self._hash(item)
        self._data[index].append(item)
        
        # Keep track of number of items in hash table
        self.n_items += 1
   
    def __repr__(self):
        output = 'ChainingHashTable:\n'.format(self.n_slots)
        for i in range(self.n_slots):
            list_at_slot = self._data[i]
            output = output+'slot {0:8d} = '.format(i)
            if list_at_slot == None:
                output = output + 'None'
            else:    
                output = output + str(list_at_slot)             
            output += '\n'
        load_factor = float(self.n_items)/self.n_slots
        output += 'n_slots = {0:d}\n'.format(self.n_slots)
        output += 'n_items in table = {0:d}\n'.format(self.n_items)
        output += 'Load factor = {0:6.3f}\n'.format(load_factor)
        return output
    
    def __contains__(self, item):
        """
        Checks to see if an item is stored within the hashtable.
        You can call this method using Python's 'in' keyword:
            ht = HashTable()
            ...
            if 'foo' in ht:
                ...
        """
        # remember self._data[index] contains a list of items that hash to 
        # the slot at the given index
        # ---start student section---
        index = self._hash(item)
        return item in self._data[index]
        # ===end student section===





#---------------------------------------------
class LinearHashTable():
    """A simple Open Addressing HashTable with Linear Probing.
    Called simply LinearHashTable to make the name shorter...
    
    >>> hash_table = LinearHashTable(11)
    >>> hash_table.store('Paul')
    >>> hash_table.store('Peter')
    >>> hash_table.store('Paula')
    >>> hash_table.store('David')
    >>> hash_table.store('Bobby')
    >>> hash_table.store('Dianna')
    >>> print(hash_table)
    LinearHashTable:
    slot        0 = David
    slot        1 = Paul
    slot        2 = -
    slot        3 = -
    slot        4 = Peter
    slot        5 = Paula
    slot        6 = -
    slot        7 = -
    slot        8 = -
    slot        9 = Bobby
    slot       10 = Dianna
    n_slots = 11
    n_items in table = 6
    Load factor =  0.545
    <BLANKLINE>
    >>> print('Peter' in hash_table)
    True
    >>> print('Dingus' in hash_table)
    False
    """
    def __init__(self, slots=11):
        """
        Creates a new hashtable with the given number of slots.
        Remember we can't have a load factor greater than 1 for an open hash...
        """
        self._data = [None for i in range(slots)]
        self.n_slots = slots
        self.n_items = 0
    
    def _next_free_slot(self, old_hash, item):
        """Keeps incrementing hash index until an empty slot is found.
        Then returns the index of that slot"""
        curr_index = old_hash
        #print self._data
        while self._data[curr_index] != None:
            curr_index = (curr_index+1)%self.n_slots
            if (curr_index == old_hash):  # have wrapped back to start
                if self._data[curr_index] == item:
                    print('Item already in HashTable')
                else:
                    #shouldn't get here as store method checks for full table
                    #Argh - crash, who made the hashtable too small?
                    #print self._data
                    print('Size = ' + str(self.n_slots))
                    print('Number of items = ' + str(self.n_items))
                    print("Hash table is full!!!! You eeediot")
                    raise IndexError("Hash table is full!!!!")
        return curr_index
    
    def store(self, item):
        """Stores an item in the hashtable."""
        if self.n_slots == self.n_items:
            #Argh - crash, who made the hashtable too small?
                print(self._data)
                print('Size = ' + str(self.n_slots))
                print('Slots used = ' + str(self.n_items))
                print("Hash table is full!!!! You eeediot")
                print("A good Hasher would have resized the hash table by now!")
                raise IndexError ("Hash table is full!!!!")
        # ***********************************************************
        # ---start student section---
        index = self._hash(item)
        if self._data[index] == '-':
            self._data[index] = item
        else:
            new_index = self._next_free_slot(index, item)
            self._data[new_index] = item
        
        # ===end student section===

        # Keep track of number of items in hash table
        self.n_items += 1
    
    def _hash(self, item):
        """Computes the hash of an item."""
        return nice_hash(item) % self.n_slots
        
    def __contains__(self, item):
        """
        Checks to see if an item is stored within the hashtable.
        You can call this method using Python's 'in' keyword:
            ht = HashTable()
            ...
            if 'foo' in ht:
                ...
        """
        first_hash = self._hash(item)
        have_wrapped = False
        if self._data[first_hash] == item:
            return True
        else:
            current_index = first_hash
            while self._data[current_index] != None:
                if self._data[current_index] == item:
                    # horay we found it
                    return True
                if (current_index == first_hash) and have_wrapped:
                        # back to original hash and didn't find item
                        # phew - the hashtable is full!
                        return False
                if current_index == (self.n_slots-1):
                        # wrap back to start of hash table
                        current_index = 0
                        have_wrapped = True
                else:
                    current_index += 1

    def __repr__(self):
        output = 'LinearHashTable:\n'
        for i in range(self.n_slots):
            output += 'slot {0:8d} = '.format(i)
            item = self._data[i]
            if item == None:
                output = output + '-'
            else:
                output = output + str(item)
            output += '\n'
        load_factor = float(self.n_items)/self.n_slots
        output += 'n_slots = {0:d}\n'.format(self.n_slots)
        output += 'n_items in table = {0:d}\n'.format(self.n_items)
        output += 'Load factor = {0:6.3f}\n'.format(load_factor)
        return output



#---------------------------------------------
class QuadraticHashTable():
    """Is a child class of OpenAddressHashTable.
    If a collision then uses a quadratic probing function to find a free slot
    >>> hash_table = QuadraticHashTable(11)
    >>> hash_table.store('Paul')
    >>> hash_table.store('Peter')
    >>> hash_table.store('Paula')
    >>> hash_table.store('David')
    >>> hash_table.store('Bobby')
    >>> hash_table.store('Dianna')
    >>> hash_table.store('Dirk')
    >>> hash_table.store('Darlene')
    >>> print(hash_table)
    QuadraticOpenAddressHashTable:
    slot        0 = David
    slot        1 = Paul
    slot        2 = Darlene
    slot        3 = -
    slot        4 = Peter
    slot        5 = Paula
    slot        6 = Dirk
    slot        7 = -
    slot        8 = -
    slot        9 = Bobby
    slot       10 = Dianna
    n_slots = 11
    n_items in table = 8
    Load factor =  0.727
    <BLANKLINE>
    >>> print('Dirk' in hash_table)
    True
    >>> print('Dingle' in hash_table)
    False
    """
    
    def __init__(self, slots=11):
        """
        Creates a new hashtable with a number of slots (default: 10).
        Remember we can't have a load factor greater than 1 for an open hash...
        """
        self._data = [None for i in range(slots)]
        self.n_slots = slots
        self.n_items = 0
    
    def _next_free_slot(self, first_hash, item):
        """Keeps incrementing hash index until an empty slot is found.
        Then returns the index of that slot"""
        curr_index = first_hash
        try_number = 0
        tried=[]
        #print self._data
        while self._data[curr_index] != None:
            tried.append(curr_index)
            if try_number+1 == self.n_slots:
                #print self._data
                print('Size = ' + str(self.n_slots))
                print('Number of items = ' + str(self.n_items))
                print("Failed to find an empty slot...")
                print('Try number = '+str(try_number))
                print('List of tried slots = '+str(tried))
                print('Current table = '+str(self._data))
                raise ValueError ("Failed to find an empty slot!!!!")
            else:
                try_number += 1
                curr_index = (first_hash+try_number**2)%self.n_slots
        #print 'Try number = '+str(try_number)
        #print 'List of tried slots = '+str(tried)
        #print 'Current table = '+str(self._data)
        return curr_index
    
    
    def store(self, item):
        """Stores an item in the hashtable."""
        if self.n_slots == self.n_items:
            #Argh - crash, who made the hashtable too small?
                print(self._data)
                print('Size = ' + str(self.n_slots))
                print('Slots used = ' + str(self.n_items))
                print("Hash table is full!!!! You eeediot")
                print("A good Hasher would have resized the hash table by now!")
                raise ValueError ("Hash table is full!!!!")
        # **************************************************
        # Write your spell check code here 
        # ---start student section---
        index = self._hash(item)
        if self._data[index] == '-':
            self._data[index] = item
        else:
            new_index = self._next_free_slot(index, item)
            self._data[new_index] = item        
        # ===end student section===
        self.n_items += 1
        
    def _hash(self, item):
        """Computes the hash of an item."""
        return nice_hash(item) % self.n_slots
 
    def __contains__(self, item):
        """
        Checks to see if an item is stored within the hashtable.
        You can call this method using Python's 'in' keyword:
            ht = HashTable()
            ...
            if 'foo' in ht:
                ...
        """
        first_hash = self._hash(item)
        try_number = 0
        current_index = first_hash
                
        while self._data[current_index] != None:
            if self._data[current_index] == item:
                #horay we found it
                return True
            #check to see if we have reached end of possible slots
            #return if we have
            if try_number == self.n_slots:
                return False
            try_number += 1
            current_index = (first_hash+try_number**2)%self.n_slots
        #got to first empty slot in sequence, so item isn't in hash table
        return False
                

    
    def __repr__(self):
        output = 'QuadraticOpenAddressHashTable:\n'
        for i in range(self.n_slots):
            output += 'slot {0:8d} = '.format(i)
            item = self._data[i]
            if item == None:
                output = output + '-'
            else:
                output = output + str(item)
            output += '\n'
        load_factor = float(self.n_items)/self.n_slots
        output += 'n_slots = {0:d}\n'.format(self.n_slots)
        output += 'n_items in table = {0:d}\n'.format(self.n_items)
        output += 'Load factor = {0:6.3f}\n'.format(load_factor)
        return output
#==============================================








#---------------------------------------------
def spellcheck_with_list(document, dictionary):
    """
    Checks the spelling of each word in 'document' (a list of words) against
    the dictionary (another list of words).
    """
    #Check all words in the document list
    #Printing out misspelled words and counting them
    print('-----------------')
    print('Misspelled words:')
    print('-----------------')
    num_errors = 0
    start_check_time = clock()
   
    # *****************************************
    # Write your spell check code here 
    # ---start student section---
    duplicates = set()
    for word in document:
        if word not in dictionary: 
            num_errors += 1
            print(word)
            duplicates.add(word)
    print(len(duplicates))
    # ===end student section===
    end_check_time = clock()
    
    print('---------------------')
    print('Number of errors = {0:d} words'.format(num_errors))  
    print('=====================\n')    
    check_time = end_check_time - start_check_time
    ms_per_word = (check_time/len(document))*1000
    print('-------------------------------------------')
    print('Summary stats (using simple linear search):')
    print('-------------------------------------------')    
    print('Input file length = {0:d} words'.format(len(document)))
    print('Document check time = {0:8.4f}s'.format(check_time))
    print('Check time per word in document = ', end='')
    print('{0:10.6f}ms\n\n'.format(ms_per_word))





#---------------------------------------------
def spellcheck_with_hashtable(document, dictionary, ht_type, ht_size):
    """
    Checks the spelling of each word in 'document' (a list of words) against
    the dictionary (another list of words, using the given hash_table).
    
    """
    #Build Hash Table by adding words from the dictionary list
    start_build_time = clock()
    if ht_type == 'Chaining':
        hash_table = ChainingHashTable(ht_size)
    elif ht_type == 'Linear':
        hash_table = LinearHashTable(ht_size)
    elif ht_type == 'Quadratic':
        hash_table = QuadraticHashTable(ht_size)
    else:
        print('Hash type must be Chaining, Linear or Quadratic.')
    
    for word in dictionary:
        hash_table.store(word)
    end_build_time = clock()
    
    #Check all words in the document list
    #Printing out misspelled words and counting them
    print('-----------------')
    print('Misspelled words:')
    print('-----------------')
    num_errors = 0
    start_check_time = clock()
    
    # *****************************************
    # Write your spell check code here 
    # ---start student section---
    count = 0
    unique = set()
    for word in document:
        if word not in hash_table:
            num_errors += 1
            count += 1
            print(count, word)
            unique.add(word)
    print(len(unique))
    # ===end student section===
            
    end_check_time = clock()
    print('-'*50)
    print('Number of errors = {0:d} words'.format(num_errors))  
    print('='*50)
    print()
    build_time = end_build_time - start_build_time
    check_time = end_check_time - start_check_time
    load_factor = float(hash_table.n_items)/hash_table.n_slots
    ms_per_word = (check_time/len(document))*1000
    print('-'*50)
    print('Summary stats (using '+ht_type+' hash table):')
    print('-'*50)    
    print('Hash table size = {0:d} slots'.format(hash_table.n_slots))
    print('Input file length = {0:d} words'.format(len(document)))
    print('Hash table load factor = {0:8.4f}'.format(load_factor))
    print('Hash table build time = {0:8.4f}s'.format(build_time))
    print('Document check time = {0:8.4f}s'.format(check_time))
    print('Check time per word in document = ', end='')
    print('{0:10.6f}ms\n\n'.format(ms_per_word))




           
def binary_search(values, needle):
    lowerBound = 0
    upperBound = len(values)
    index = 0
    # ---start student section---
    pass
    # ===end student section===
    return False

# ------------------------------------------------
def spellcheck_bin(document,dictionary):
    #Check all words in the document list
    #Printing out misspelled words and counting them
    print('-----------------')
    print('Misspelled words:')
    print('-----------------')
    num_errors = 0
    
    dict_sort_start = clock()
    dictionary = sorted(dictionary)
    dict_sort_end = clock()
    
    start_check_time = clock()    
    for word in document:
        if not binary_search(dictionary, word):
            print(word)
            num_errors += 1
    end_check_time = clock()

    print('---------------------')
    print('Number of errors = {0:d} words'.format(num_errors))  
    print('=====================\n')
    
    check_time = end_check_time - start_check_time
    ms_per_word = (check_time/len(document))*1000
    dict_sort_time = dict_sort_end - dict_sort_start
    print('--------------------------------------------------')
    print('Summary stats (using Binary Search on Dictionary):')
    print('--------------------------------------------------')    
    print('Input file length = {0:d} words'.format(len(document)))
    print('Dictionary sort time = {0:8.4f}s'.format(dict_sort_time))
    print('Document check time = {0:8.4f}s'.format(check_time))
    print('Check time per word in document = ', end='')
    print('{0:10.6f}ms\n\n'.format(ms_per_word))
    
    
if __name__ == '__main__':
    os.environ['TERM'] = 'linux' # Suppress ^[[?1034h to keep doctests happy
    
    doctest.testmod(report=True)

    # if you want to run one set of doctests at a time you can comment out the above
    # testmod line and uncomment the run_docstring_examples line below
    # then change the class name to whichever class you want to test.
    
    # doctest.run_docstring_examples(ChainingHashTable,globals())
