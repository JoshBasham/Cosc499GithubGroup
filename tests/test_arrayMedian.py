from scripts.median import median
import unittest

class TestMedian(unittest.TestCase):
    def testMedian(self):
        actual = median(nums=[3, 6, 9, 13, 17, 23, 40, 20, 13, 8])
        excepted = 20.0
        self.assertEqual(actual, excepted)