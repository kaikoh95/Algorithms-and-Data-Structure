"""Module for detecting voter fraud using merging."""
from classes import VoterList

def fraud_detect_merge(first_booth_voters, second_booth_voters):
    """This function takes a VoterList from two voting booths and returns a new
    VoterList, the voters who cast a vote in both booths, and an integer, the
    number of VoterName comparisons the function made. Both VoterLists are in
    lexicographical order."""

    fraud_list = VoterList()
    count = 0
    pos1 = 0
    pos2 = 0
    first_len = len(first_booth_voters)
    second_len = len(second_booth_voters)
    while pos1 < first_len and pos2 < second_len:
        first = first_booth_voters[pos1]
        second = second_booth_voters[pos2]        
        count += 1
        if first == second:
            fraud_list.append(second)             
            pos1 += 1
            pos2 += 1              
        else:
            count += 1
            if first < second:
                pos1 += 1
            else:
                pos2 += 1
    return fraud_list, count