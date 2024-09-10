import unittest
from typing import List
from Q2 import merge
from ed_utils.decorators import number
from tests.conversions import AR


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
        self.customAssertEqual(merge(AR([1,2,4]), AR([1,3,4])), AR([1,1,2,3,4,4]))
        self.customAssertEqual(merge(AR([1,4,6,7,11]), AR([5,9])), AR([1,4,5,6,7,9,11]))

    @number("2.2")
    def test_extra(self):
        self.customAssertEqual(merge(AR([2,3,5]), AR([1,4,6])), AR([1,2,3,4,5,6]))
        self.customAssertEqual(merge(AR([10,20,30]), AR([15,25,35])), AR([10,15,20,25,30,35]))
        self.customAssertEqual(merge(AR([100,200,300]), AR([150,250,350])), AR([100,150,200,250,300,350]))
        

if __name__ == '__main__':
    unittest.main()