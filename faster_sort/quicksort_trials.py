import time
import random
from quicksort import *
from matplotlib import pyplot
import sys

# Get the time units given by the perf_counter
# Note: time.clock has been deprecated in Python 3.3
# and replaced with the more precise perf_counter method

# define time.get_time to be the appropriate time counter
if sys.version_info < (3, 3):
    get_time = time.clock
    print("Using time.clock for timing - Python ver < 3.3")
else:
    get_time = time.perf_counter
    print("Using time.perf_counter for timing - Python ver >= 3.3")
    REZ = time.get_clock_info('perf_counter').resolution
    print('One unit of time is ' + str(REZ) + ' seconds')


list_of_ns = list(range(40, 800, 40))
n_trials = 100
avg_times_sorted = []

for n in list_of_ns:
    total_time_sorted = 0
    for i in range(n_trials):
        x = [1]*760
        #random.shuffle(x)  
        start = get_time()
        s = quicksort(x, 'left-pivot')
        end = get_time()
        time_taken = end - start
        total_time_sorted += time_taken
    avg_time_sorted = total_time_sorted / n_trials
    avg_times_sorted.append(avg_time_sorted)

pyplot.plot(list_of_ns, avg_times_sorted, 'bo')
pyplot.title("Time vs. List size, average of {0} trials".format(n_trials))
pyplot.xlabel('n')
pyplot.ylabel('Average Time per sort')
pyplot.show()
