"""Module for reading test data."""
from classes import VoterName, VoterList
import random

RANDOM_SEED = 17
random.seed(RANDOM_SEED)

def read_test_data(filename):
    """Reads a test data file and returns a triple containg first booth voters,
    second booth voters and voters comitting fraud by voting in both booths."""
    first_booth_voters = VoterList()
    second_booth_voters = VoterList()
    fraud_voters = VoterList()
    with open(filename) as test_data_file:
        #Read first booth voter names
        current_line = _get_next_line(test_data_file)
        first_booth_voters_size = int(current_line)
        for _ in range(first_booth_voters_size):
            current_line = _get_next_line(test_data_file)
            first_booth_voters.append(VoterName(current_line))

        #Read second booth voter names
        current_line = _get_next_line(test_data_file)
        second_booth_voters_size = int(current_line)
        for _ in range(second_booth_voters_size):
            current_line = _get_next_line(test_data_file)
            second_booth_voters.append(VoterName(current_line))

        #Read voter names that commited fraud
        current_line = _get_next_line(test_data_file)
        fraud_voters_size = int(current_line)
        for _ in range(fraud_voters_size):
            current_line = _get_next_line(test_data_file)
            fraud_voters.append(VoterName(current_line))

    return first_booth_voters, second_booth_voters, fraud_voters

def _get_next_line(test_data_file):
    """Reads and returns one line from a test data file. Returns None if the end
    of file is reached."""
    current_line = test_data_file.readline()
    #Comment lines are not read.
    while current_line.startswith('#'):
        current_line = test_data_file.readline()
    #None is returned if the end of the file is reached.
    if len(current_line) == 0:
        return None
    return current_line.strip()

def shuffle_voter_list(voters):
    """Randomises the order of the VoterNames in the VoterList voters."""
    for index in range(len(voters)):
        _swap(voters, index, random.randrange(index, len(voters)))

def _swap(voters, first, second):
    """Swaps the voters at indexes first and second."""
    voters[first], voters[second] = voters[second], voters[first]