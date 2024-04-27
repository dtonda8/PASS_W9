import unittest
from typing import List
from Q2 import merge
from ed_utils.decorators import number
from tests.conversions import AL


class Test_Q2(unittest.TestCase):
    def customAssertEqual(self, actual: List[int], expected: List[int]):
        if len(actual) != len(expected):
            self.fail(f"Actual length, {len(actual)}, doesn't match expected length, {len(expected)}")
        elif len(actual) == len(expected) == 0:
            return
        if not ((actual[0] == expected[0] and actual[1] == expected[1]) or (actual[1] == expected[0] and actual[0] == expected[1])):
            self.fail(f"Actual elements ({actual[0]}, {actual[1]}) does match expected elements ({expected[0]}, {expected[1]})")

    @number("2.1")
    def test_examples(self):
        self.customAssertEqual(merge(AL([1,2,4]), AL([1,3,4])), AL([1,1,2,3,4,4]))
        self.customAssertEqual(merge(AL([1,4,6,7,11]), AL([5,9])), AL([1,4,5,6,7,9,11]))
        self.customAssertEqual(merge(AL([]), AL([])), AL([]))

    @number("2.2")
    def test_extra(self):
        self.customAssertEqual(merge(AL([2,3,5]), AL([1,4,6])), AL([1,2,3,4,5,6]))
        self.customAssertEqual(merge(AL([10,20,30]), AL([15,25,35])), AL([10,15,20,25,30,35]))
        self.customAssertEqual(merge(AL([100,200,300]), AL([150,250,350])), AL([100,150,200,250,300,350]))
        

if __name__ == '__main__':
    unittest.main()