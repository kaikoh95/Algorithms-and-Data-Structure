"""Lab array classes"""

#------------------------------------------------------------------------
class LinearArray():
    """Implements an array using an un-ordered Python list."""

    def __init__(self):
        self.data = list()  # Create the list to store the data
        self.comparisons = 0  # Reset comparison counter

    def insert(self, value):
        """Adds an item to the end of the array"""
        self.comparisons = 0
        # Add the item to the end of the data list
        self.data.append(value)

    def remove(self, value):
        """Removes the first occurance of value in the array."""
        # Look for the index in the list that 
        # contains the element to delete
        index = self.find_index(value)

        # If we've found the item...
        if not index is None:
            # Delete it from the list
            del self.data[index]

    def contains(self, value):
        """Returns true if the array contains the value, else returns None."""
        return (not self.find_index(value) is None)

    def find_index(self, value):
        """
        Finds the index of the given value in the data list.
        Returns either the index of the item in the list, or None if
        the item doesn't exist.
        """
        # Counter for how many comparisons are done
        self.comparisons = 0
        for i in range(len(self.data)): # Loop through each item in the data list
            self.comparisons += 1# Add one to comparisons for each comparison
        # involving a list element
            # If the item is equal to our search value
            # return the index this item is at
            if self.data[i] == value: 
                return i
        # If we loop through everything and haven't found
        # the item, return None
        return None        

    def __str__(self):
        """
        Prints out all the values in the array
        """
        string = ''
        for i, value in enumerate(self.data):
            string += '{} , {}\n'.format(i, value)
        return string





#------------------------------------------------------------------------
class SortedArray():

    """Implements an array using a Python list, but stores the items in
    sorted order (rather than the order they are inserted). """

    def __init__(self):
        self.data = list()
        self.comparisons = 0

    def insert(self, value):
        """Inserts an item in to the array in its sorted position"""
        # Find the correct index to insert value using a binary search
        self.comparisons = 0
        lowerBound = 0
        upperBound = len(self.data)
        index = 0
        # When these cross, they're at the index the item should be at
        while lowerBound < upperBound:
            self.comparisons += 1
            index = (lowerBound + upperBound) // 2
            if self.data[index] < value:
                lowerBound = index + 1  # Look in the upper half
            else:
                upperBound = index     # Look in the lower half
        self.data.insert(lowerBound, value)

    def remove(self, value):
        """Removes the first occurance of value in the array."""
        # Find the index to remove
        idx = self.find_index(value)
        # If we've found the item...
        if not idx is None:
            # Delete it from the list
            # (this will shuffle all of the higher items down for us)
            del self.data[idx]

    def contains(self, value):
        """Returns true if the array contains the value, else returns None"""
        return (not self.find_index(value) is None)

    def find_index(self, value):
        """ Finds the index of the given value in the data list.
        Returns either the index of the item in the list, or None if
        the item doesn't exist.
        """
        self.comparisons = 0
        lowerBound = 0
        upperBound = len(self.data)
        index = 0
        while lowerBound < upperBound:
            index = (lowerBound + upperBound) // 2
            self.comparisons += 1
            if self.data[index] == value:  # Found it!
                return index
            if self.data[index] < value:
                lowerBound = index + 1  # Look in the upper half
            else:
                upperBound = index     # Look in the lower half
            self.comparisons += 1

        # If we haven't found it by now, it doesn't exist
        return None

    def __str__(self):
        """
        Prints out all the values in the array
        """
        string = ''
        for i, value in enumerate(self.data):
            string += '{} , {}\n'.format(i, value)
        return string






#------------------------------------------------------------------------
class BitVectorArray():

    """Implements an array using a variation on a bit vector (bitmap)."""

    def __init__(self, maxValue):
        """
        Creates a new BitVectorArray.
        maxValue is the largest integer value that can be stored in this set.
        """
        self.data = [0 for n in range(maxValue + 1)]
        self.comparisons = 0

    def remove(self, value):
        """Removes an occurance of the value in the array."""
        self.comparisons = 0
        if self.data[value]:
            self.data[value] -= 1

    def insert(self, value):
        self.data[value] += 1

    def contains(self, value):
        """Returns true if the array contains the value, else returns None"""
        return self.data[value] > 0

    def __str__(self):
        """Prints out all the values in the array."""
        string = ''
        for i, value in enumerate(self.data):
            string += '{} , {}\n'.format(i, value)
        return string
