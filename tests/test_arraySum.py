import unittest
from scripts.arraySum import arraySum

nums = [3, 6, 9, 13, 17, 23, 40, 20, 13, 8]

class TestArraySumFunction(unittest.TestCase):
    def test_array_sum_success(self):
        actual = arraySum(nums)
        expected = 152
        self.assertEqual(actual, expected)
