import sys
import time
from Structures import Stack, Queue

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
    
    
    
# Do some testing here, sing get_time() to get start and end times
