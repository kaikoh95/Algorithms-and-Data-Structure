'''Compare search times with Python's inbuilt lists and dictionaries.'''
import sys
import time
import random
import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot


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



def run_list_trials(num_trials=1):
    """ Creates empty lists of increasing size
    then searches for a randomly generated number in each list.
    Note: we are being nice here is that the number will be in the list...
    Returns two lists, the first contains all the list sizes tried and
    the second contains the average time per locate operation for each list size. """
    list_of_times = []
    # we will test for sizes [20000, 40000, 60000, etc...]
    list_of_sizes = list(range(20000, 1000001, 20000))
    for list_size in list_of_sizes:
        num_list = list(range(list_size))  # creates a list of n items

        # run trials, each on simply trying to locate the number in the list
        start = get_time()
        for i in range(num_trials):
            # try to find random number (between 1 and n) in the list
            value_to_find = random.randrange(list_size)
            found = value_to_find in num_list
        end = get_time()

        # print number of trials and time taken (with a tab in between)
        time_taken_per_locate = (end - start) / num_trials
        print(("{}\t{:>10.8f}" .format(list_size, time_taken_per_locate)))

        # keep track of all the times
        list_of_times.append(time_taken_per_locate)
    return list_of_sizes, list_of_times


def run_dictionary_trials(num_trials=1):
    """ Creates an empty Dictionary and search for a randomly generated number
    in the dictionary.
    Note: we are being nice here is that the number will be in the dict..."""
    list_of_times = []
    list_of_sizes = list(range(20000, 1000001, 20000))
    for dict_size in list_of_sizes:
        # fill test_dict dictionary with n items {1: None, 2: None, 3: None...}
        test_dict = {i: None for i in range(dict_size)}

        # repeat the following num_trials times:
        #   check whether a randomly generated number is in the dictionary
        # ---start student section---
        pass
        # ===end student section===
        # keep track of all the times
        list_of_times.append(time_taken_per_locate)
    return list_of_sizes, list_of_times



def graph_one_series_example():
    """An example of how to graph two series."""
    n_trials = 10
    x1, y1 = run_list_trials(n_trials)
    pyplot.plot(x1, y1, 'bo')   # use blue o's as markers
    pyplot.title("List Locate Testing, {0} Trial runs".format(n_trials))
    pyplot.xlabel('n')
    pyplot.ylabel('Average Time per locate')
    pyplot.show()


def graph_two_series_example():
    """An example of how to graph two series."""
    n_trials = 10
    x1, y1 = run_list_trials(n_trials)
    x2, y2 = run_dictionary_trials(n_trials)

    pyplot.plot(x1, y1, 'bo', x2, y2, 'ro') # use blue and red o's
    pyplot.title("List Locate Testing, {0} Trial runs".format(n_trials))
    pyplot.xlabel('n')
    pyplot.ylabel('Average Time per locate')
    pyplot.show()



def run_tests():
    '''Function that runs various tests. Put your test calls in here'''
    number_of_trials = 10
    print("LIST TRIAL RUN")
    print("Averages over ", number_of_trials, " trials.")
    print('size(n)\tAvg. Time')
    sizes, times = run_list_trials(number_of_trials)


if __name__ == "__main__":
    run_tests()

    # graph_one_series_example()
    # graph_two_series_example()
