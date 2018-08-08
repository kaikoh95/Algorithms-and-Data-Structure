"""Module for detecting voter fraud using binary search."""
from classes import VoterList

def fraud_detect_bin(first_booth_voters, second_booth_voters):
    """This function takes a VoterList from two voting booths and returns a new
    VoterList, the voters who cast a vote in both booths, and an integer, the
    number of VoterName comparisons the function made. The second VoterList is
    in lexicographical order."""
    
    fraud_list = VoterList()
    count = 0
    for voter in first_booth_voters:
        lower = 0
        upper = len(second_booth_voters)
        mid = (lower + upper) // 2
        while lower < upper:
            count += 1
            if second_booth_voters[mid] < voter:
                lower = mid + 1
            else:               
                upper = mid
            mid = (lower + upper) // 2
        if mid < len(second_booth_voters):
            count += 1
            if second_booth_voters[mid] == voter:
                fraud_list.append(voter)
    return fraud_list, count