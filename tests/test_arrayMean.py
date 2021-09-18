import unittest

#scripts/arrayMean.py
from scripts.arrayMean import arrayMean

class TestArrayMean(unittest.TestCase):
    def test_arrayMean(self):
        nums = [3, 6, 9, 13, 17, 23, 40, 20, 13, 8]
        actual = arrayMean(nums)
       # print(actual)
        expected = 15.2
        self.assertEqual(actual, expected)