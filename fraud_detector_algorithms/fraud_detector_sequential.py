"""Module for detecting voter fraud using sequential search."""
from classes import VoterList

def fraud_detect_seq(first_booth_voters, second_booth_voters):
    """This function takes a VoterList from two voting booths and returns a new
    VoterList, the voters who cast a vote in both booths, and an integer, the
    number of VoterName comparisons the function made. The VoterLists are
    un-ordered."""
    
    fraud_list = VoterList()
    count = 0
    for voter1 in first_booth_voters:
        for voter2 in second_booth_voters:
            count += 1
            if voter1 == voter2:
                fraud_list.append(voter1)
                break
    return fraud_list, count