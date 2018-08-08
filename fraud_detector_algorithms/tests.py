"""Module containing the unit tests for the fraud detection algorithms."""
import unittest
import math
from classes import VoterName, VoterList, VoterHashTable
from fraud_detector_sequential import fraud_detect_seq
from fraud_detector_binary1 import fraud_detect_bin
from fraud_detector_merge import fraud_detect_merge
from fraud_detector_hash import fraud_detect_hash
from tools import read_test_data

class BaseTestFraudDetector(unittest.TestCase):
    def setUp(self):
        """This runs before each test case"""
        VoterList.reset_comparisons()

    def fraud_list_test(self, test_file_location, fraud_detect_algorithm):
        first_booth_voters, second_booth_voters, fraud_voters = read_test_data(test_file_location)
        fraud_found, comparisons = fraud_detect_algorithm(first_booth_voters,
                                                          second_booth_voters)
        self.assertEqual(fraud_found, fraud_voters)
        self.assertEqual(type(fraud_found), type(fraud_voters))

    def internal_comparisons_test(self, test_file_location, fraud_detect):
        first_booth_voters, second_booth_voters, fraud_voters = read_test_data(test_file_location)
        fraud_found, comparisons = fraud_detect(first_booth_voters,
                                                second_booth_voters)
        self.assertEqual(comparisons, VoterList.get_comparisons())

    def comparisons_test(self, test_file_location, fraud_detect, expected_comparisons):
        first_booth_voters, second_booth_voters, fraud_voters = read_test_data(test_file_location)
        fraud_found, comparisons = fraud_detect(first_booth_voters,
                                                second_booth_voters)
        self.assertEqual(comparisons, expected_comparisons)

    def comparisons_within_bound_test(self, test_file_location, fraud_detect):
        first_booth_voters, second_booth_voters, fraud_voters = read_test_data(test_file_location)
        fraud_found, comparisons = fraud_detect(first_booth_voters, second_booth_voters)
        lower_bound, upper_bound = self.get_bounds(len(first_booth_voters),
                                                   len(second_booth_voters),
                                                   len(fraud_voters))
        self.assertGreaterEqual(comparisons, lower_bound)
        self.assertLessEqual(comparisons, upper_bound)

    def test_no_fraud_small(self):
        file_location = 'TestData/test_data10-10-0.txt'
        self.fraud_list_test(file_location)

    def test_single_fraud_small(self):
        file_location = 'TestData/test_data10-10-1.txt'
        self.fraud_list_test(file_location)

    def test_all_fraud_small(self):
        file_location = 'TestData/test_data10-10-10.txt'
        self.fraud_list_test(file_location)

    def test_no_fraud_small_internal_comparisons(self):
        file_location = 'TestData/test_data10-10-0.txt'
        self.internal_comparisons_test(file_location)

    def test_single_fraud_small_internal_comparisons(self):
        file_location = 'TestData/test_data10-10-1.txt'
        self.internal_comparisons_test(file_location)

    def test_all_fraud_small_internal_comparisons(self):
        file_location = 'TestData/test_data10-10-10.txt'
        self.internal_comparisons_test(file_location)

    def test_no_fraud_small_comparisons_within_bound(self):
        file_location = 'TestData/test_data10-10-0.txt'
        self.comparisons_within_bound_test(file_location)

    def test_single_fraud_small_comparisons_within_bound(self):
        file_location = 'TestData/test_data10-10-1.txt'
        self.comparisons_within_bound_test(file_location)
    
    def test_all_fraud_small_comparisons_within_bound(self):
        file_location = 'TestData/test_data10-10-10.txt'
        self.comparisons_within_bound_test(file_location)

    def test_no_fraud_big_comparisons_within_bound(self):
        file_location = 'TestData/test_data1000-1000-0.txt'
        self.comparisons_within_bound_test(file_location)

    def test_single_fraud_big_comparisons_within_bound(self):
        file_location = 'TestData/test_data1000-1000-1.txt'
        self.comparisons_within_bound_test(file_location)

    def test_all_fraud_big_comparisons_within_bound(self):
        file_location = 'TestData/test_data1000-1000-10.txt'
        self.comparisons_within_bound_test(file_location)        

    def test_no_fraud_big(self):
        file_location = 'TestData/test_data1000-1000-0.txt'
        self.fraud_list_test(file_location)

    def test_single_fraud_big(self):
        file_location = 'TestData/test_data1000-1000-1.txt'
        self.fraud_list_test(file_location)

    def test_all_fraud_big(self):
        file_location = 'TestData/test_data1000-1000-10.txt'
        self.fraud_list_test(file_location)



class TestFraudDetectorSequential(BaseTestFraudDetector):
    def fraud_list_test(self, test_file_location):
        super().fraud_list_test(test_file_location, fraud_detect_seq)

    def comparisons_test(self, test_file_location, comparisons):
        super().comparisons_test(test_file_location, fraud_detect_seq, comparisons)

    def internal_comparisons_test(self, test_file_location):
        super().internal_comparisons_test(test_file_location, fraud_detect_seq)

    def comparisons_within_bound_test(self, test_file_location):
        super().comparisons_within_bound_test(test_file_location, fraud_detect_seq)

    def get_bounds(self, first_booth_size, second_booth_size, fraud_size):
        lower_bound = 1
        upper_bound = first_booth_size * second_booth_size
        return lower_bound, upper_bound

    def test_no_fraud_small_comparisons(self):
        file_location = 'TestData/test_data10-10-0.txt'
        self.comparisons_test(file_location, 100)

    def test_single_fraud_small_comparisons(self):
        file_location = 'TestData/test_data10-10-1.txt'
        self.comparisons_test(file_location, 96)

    def test_all_fraud_small_comparisons(self):
        file_location = 'TestData/test_data10-10-10.txt'
        self.comparisons_test(file_location, 55)



class TestFraudDetectorBinary(BaseTestFraudDetector):
    def fraud_list_test(self, test_file_location):
        super().fraud_list_test(test_file_location, fraud_detect_bin)

    def comparisons_within_bound_test(self, test_file_location):
        super().comparisons_within_bound_test(test_file_location, fraud_detect_bin)

    def internal_comparisons_test(self, test_file_location):
        super().internal_comparisons_test(test_file_location, fraud_detect_bin)

    def get_bounds(self, first_booth_size, second_booth_size, fraud_size):
        log2 = int(math.log(second_booth_size, 2))
        lower_bound = first_booth_size * (log2 + 1) - 2
        upper_bound = first_booth_size * (log2 + 2) + 2
        return lower_bound, upper_bound



class TestFraudDetectorMerge(BaseTestFraudDetector):
    def fraud_list_test(self, test_file_location):
        super().fraud_list_test(test_file_location, fraud_detect_merge)

    def comparisons_within_bound_test(self, test_file_location):
        super().comparisons_within_bound_test(test_file_location, fraud_detect_merge)

    def internal_comparisons_test(self, test_file_location):
        super().internal_comparisons_test(test_file_location, fraud_detect_merge)

    def get_bounds(self, first_booth_size, second_booth_size, fraud_size):
        lower_bound = min(first_booth_size, second_booth_size)
        upper_bound = 2 * (first_booth_size + second_booth_size - 1)
        return lower_bound, upper_bound



class TestFraudDetectorHash(BaseTestFraudDetector):
    def setUp(self):
        VoterList.reset_comparisons()
        VoterHashTable.reset_hashes()
        VoterHashTable.reset_memory_used()

    def fraud_list_test(self, test_file_location):
        super().fraud_list_test(test_file_location, fraud_detect_hash)

    def comparisons_within_bound_test(self, test_file_location):
        super().comparisons_within_bound_test(test_file_location, fraud_detect_hash)

    def internal_comparisons_test(self, test_file_location):
        super().internal_comparisons_test(test_file_location,
                                          fraud_detect_hash)

    def memory_test(self, test_file_location, bound):
        first_booth_voters, second_booth_voters, fraud_voters = read_test_data(test_file_location)
        fraud_found, comparisons = fraud_detect_hash(first_booth_voters,
                                                     second_booth_voters)
        self.assertEqual(VoterHashTable.get_memory_used(), bound)

    def hash_test(self, test_file_location):
        first_booth_voters, second_booth_voters, fraud_voters = read_test_data(test_file_location)
        fraud_found, comparisons = fraud_detect_hash(first_booth_voters,
                                                     second_booth_voters)
        expected = len(first_booth_voters) + len(second_booth_voters)
        self.assertEqual(VoterHashTable.get_hashes(), expected)

    def get_bounds(self, first_booth_size, second_booth_size, fraud_size):
        lower_bound = fraud_size
        upper_bound = (fraud_size + first_booth_size * .9)
        return lower_bound, upper_bound

    def test_all_fraud_large_memory(self):
        file_location = 'TestData/test_data1000-1000-10.txt'
        self.memory_test(file_location, 2000)

    def test_single_fraud_large_hashes(self):
        file_location = 'TestData/test_data1000-1000-1.txt'
        self.hash_test(file_location)

def all_tests_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestFraudDetectorSequential))
    # uncomment the next lines when ready to rumble with those tests
    suite.addTest(unittest.makeSuite(TestFraudDetectorBinary))
    suite.addTest(unittest.makeSuite(TestFraudDetectorMerge))
    suite.addTest(unittest.makeSuite(TestFraudDetectorHash))
    return suite

if __name__ == '__main__':
    test_runner = unittest.TextTestRunner(verbosity=2)
    test_runner.run(all_tests_suite())