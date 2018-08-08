"""Module for detecting voter fraud using hash tables."""
from classes import VoterList, VoterHashTable

def fraud_detect_hash(first_booth_voters, second_booth_voters):
    """This function takes a VoterList from two voting booths and returns a new
    VoterList, the voters who cast a vote in both booths, and an integer, the
    number of VoterName comparisons the function made. This function should use
    a VoterHashTable initialised to an appropreate size to represent a hash
    table, use the defualt hash function for VoterNames as a hash function and
    use chaining to resolve collisions."""

    fraud_list = VoterList()
    count = 0
    table_cap = len(second_booth_voters) * 2
    voter_hash = VoterHashTable(table_cap)
    for voter in first_booth_voters:
        voter_index = hash(voter) % table_cap
        voter_hash[voter_index].append(voter)
    for voters in second_booth_voters:
        index = hash(voters) % table_cap
        for voter in voter_hash[index]:
            count += 1
            if voters == voter:
                fraud_list.append(voters)
                break
    return fraud_list, count