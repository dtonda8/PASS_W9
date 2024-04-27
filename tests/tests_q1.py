import unittest
from Q1 import is_power_of_four
from ed_utils.decorators import number


class Test_Q1(unittest.TestCase):
    @number("1.1")
    def test_examples(self):
        self.assertTrue(is_power_of_four(64))
        self.assertFalse(is_power_of_four(0))
        self.assertFalse(is_power_of_four(-1))

    @number("1.2")
    def test_extra(self):
        self.assertTrue(is_power_of_four(1))
        self.assertTrue(is_power_of_four(4**19))
        self.assertFalse(is_power_of_four(2))
        self.assertFalse(is_power_of_four(-64))
        

if __name__ == '__main__':
    unittest.main()