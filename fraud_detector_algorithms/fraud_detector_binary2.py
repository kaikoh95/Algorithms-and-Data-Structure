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
        lowerBound = 0
        upperBound = len(second_booth_voters)
        mid = (lowerBound + upperBound) // 2
        while lowerBound < upperBound:

            count += 1
            if second_booth_voters[mid] < voter:
                lowerBound = mid + 1
            else:               
                upperBound = mid
            mid = (lowerBound + upperBound) // 2
            
        if mid < len(second_booth_voters):
            count += 1
            if second_booth_voters[mid] == voter:
                fraud_list.append(voter)
    return fraud_list, count