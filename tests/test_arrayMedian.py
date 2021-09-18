from scripts.median import median
import unittest

from scripts import median

class TestMedian(unittest.TestCase):
    def testMedian(self):
        actual = median(nums=["3","5","4"])
        excepted = {"5"}
        self.assertEqual(actual, excepted)