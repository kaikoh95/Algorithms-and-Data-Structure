"""Module containing classes for storing and comparing votes."""

class VoterList:
    """A wrapped and limited version of the list class to hold a list of
    VoterName objects."""
    _comparisons = 0

    def __init__(self):
        self.__data = []
        self.__accesses = 0

    def __getitem__(self, i):
        self.__accesses += 1
        return self.__data[i]

    def __len__(self):
        return len(self.__data)

    def __repr__(self):
        return repr(self.__data)

    def __contains__(self, item):
        raise TypeError("You can't use the 'in' keyword with a VoterList")

    def __eq__(self, other):
        comparisons_before_check = VoterList._comparisons
        equality_result = self.__data == other
        VoterList._comparisons = comparisons_before_check
        return equality_result

    def index(self, a=None):
        raise TypeError("You can't do that with a VoterList")

    def append(self, item):
        if not item is None and type(item) != VoterName:
            raise ValueError("Only VoterName objects can be put in a VoterList")
        else:
            self.__data.append(item)

    def get_accesses(self):
        return self.__accesses

    @classmethod
    def get_comparisons(cls):
        return cls._comparisons

    @classmethod
    def reset_comparisons(cls):
        cls._comparisons = 0



class VoterName:
    '''A wrapped string representing a voter name and counts comparisons of
    itself against other voter names.'''
    def __init__(self, base):
        self.__name = base

    def __eq__(self, j):
        if type(j) != VoterName:
            VoterList._comparisons += 1
        return self.__name == j

    def __le__(self, j):
        if type(j) != VoterName:
            VoterList._comparisons += 1
        return self.__name <= j

    def __ne__(self, j):
        if type(j) != VoterName:
            VoterList._comparisons += 1
        return self.__name != j

    def __lt__(self, j):
        if type(j) != VoterName:
            VoterList._comparisons += 1
        return self.__name < j

    def __gt__(self, j):
        if type(j) != VoterName:
            VoterList._comparisons += 1
        return self.__name > j

    def __ge__(self, j):
        if type(j) != VoterName:
            VoterList._comparisons += 1
        return self.__name >= j

    def __repr__(self):
        return repr(self.__name)

    def __str__(self):
        return self.__name

    def __hash__(self):
        VoterHashTable._hashes += 1
        if self.__name is None:
            return 0
        value = ord(self.__name[0]) << 7
        for char in self.__name:
            value = self.__c_mul(1000003, value) ^ ord(char)
        value = value ^ len(self.__name)
        if value == -1:
            value = -2
        return value

    def __c_mul(self, a, b):
        return ((int(a) * int(b)) & 0xFFFFFFFF)



class VoterHashTable:
    """A limited version of a hash table to hold a list of VoterList objects."""
    _hashes = 0
    _memory_used = 0

    def __init__(self, initial_size):
        self.__data = []
        for _ in range(initial_size):
            self.__data.append(VoterList())
        VoterHashTable._memory_used += initial_size

    def __getitem__(self, i):
        return self.__data[i]

    def __repr__(self):
        return repr(self.__data)

    def __len__(self):
        return len(self.__data)

    def __contains__(self, item):
        raise TypeError("You can't use the 'in' keyword with a VoterHashTables")

    def __eq__(self, other):
        comparisons_before_check = VoterList._comparisons
        equality_result = self.__data == other
        VoterList._comparisons = comparisons_before_check
        return equality_result

    def index(self, a=None):
        raise TypeError("You can't do that with a VoterHashTable")

    @classmethod
    def get_hashes(cls):
        return cls._hashes

    @classmethod
    def reset_hashes(cls):
        cls._hashes = 0

    @classmethod
    def get_memory_used(cls):
        return cls._memory_used

    @classmethod
    def reset_memory_used(cls):
        cls._memory_used = 0