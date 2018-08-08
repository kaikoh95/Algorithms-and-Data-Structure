'''Simple program for processing trace files to test arrays.'''
# Import all three classes so we can test them all
# Remember the sorted array won't count anything until you add your code
import sys
from arrays import *
import time

# Templates for various output lines
REMOVE_TEMPLATE = '{0:>10}{1:>5d}{2:>8d} comparisons'
NOT_FOUND_TEMPLATE = '{0:>8d} comparisons (not found)'
FOUND_TEMPLATE = '{0:>8d} comparisons (found)'
FIND_TEMPLATE = '{0:>10}{1:>5d}'
INSERT_TEMPLATE = '{0:>10}{1:>5d}{2:>8d} comparisons'



# Get the time units given by the perf_counter
# Note: time.clock has been deprecated in Python 3.3
# and replaced with the more precise perf_counter method

# define time.get_time to be the appropriate time counter
# eg, then use:    now = get_time() to get the appropriate time.
# NOTE: We recommend running in Python v3.3 to be consistent with lab machines

# perfcounter returns time as seconds since some arbitrary time
# so only the difference between two times is useful...

if sys.version_info < (3, 3):
    get_time = time.clock
    print("Using time.clock for timing - Python ver < 3.3")
else:
    get_time = time.perf_counter
    print("Using time.perf_counter for timing - Python ver >= 3.3")
    REZ = time.get_clock_info('perf_counter').resolution
    print('Smallest time resolution is ' + str(REZ) + ' seconds')
    




def process_file(filename, array):
    """
    Loads the array from a file. Files contain lines in the format:
        [instruction] [value]
    Valid instructions are:
        i : Insert [value]
        c : Contains [value]?
        d : Delete [value]
    [value] must be a valid positive integer.
    """
    file = open(filename)
    for i, line in enumerate(file):
        print('{:>4}: '.format(i), end='')
        instruction, value = line.split(' ')
        value = int(value)
        if instruction == 'i':
            array.insert(value)
            print(INSERT_TEMPLATE.format('insert', value, array.comparisons))
        elif instruction == 'c':
            print(FIND_TEMPLATE.format('contains', value), end='')
            if array.contains(value):
                print(FOUND_TEMPLATE.format(array.comparisons))
            else:
                print(NOT_FOUND_TEMPLATE.format(array.comparisons))
        elif instruction == 'd':
            self.remove(value)
            print(REMOVE_TEMPLATE.format('remove', value, array.comparisons))
        else:
            print('Whoops. Unknown command........')
    file.close()



def time_sorted_trial(filename):
    test_array = SortedArray()
    print('\nRunning trial on sorted array with', filename)
    start_time = get_time()
    process_file(filename, test_array)
    end_time = get_time()
    time_taken = end_time - start_time
    print("Took {0:.3f} seconds.".format(time_taken))



def main_tests():
    '''Do some file processing here...'''
    # for example
    filename = 'file3.txt'
    print('Processing', filename, 'with a Binary array')
    test_array = LinearArray()  # initialise a LinearArray
    process_file(filename, test_array)

    # Add more tests here:)




if __name__ == '__main__':
    main_tests()

