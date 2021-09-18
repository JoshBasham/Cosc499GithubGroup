import unittest

from scripts.arrayMult import mult

class TestMult(unittest.TestCase):
    def test_arrayMult(self):
        print("Test Case 1: ")
        nums = [3, 6, 9, 13, 17, 23, 40, 20, 13, 8]
        actual = mult(nums)
        expected = 68510707200
        self.assertEqual(actual, expected)
