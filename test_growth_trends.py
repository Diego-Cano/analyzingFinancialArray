import unittest
from growth_trends import sorted_squares

class TestSortedSquares(unittest.TestCase):
    def test_normal_cases(self):
        self.assertEqual(sorted_squares([-5, -2, 0, 3, 10]), [0, 4, 9, 25, 100])
        self.assertEqual(sorted_squares([-8, -3, 2, 4, 12]), [4, 9, 16, 64, 144])
        self.assertEqual(sorted_squares([-7, -4, -1, 0, 1, 5, 6]), [0, 1, 1, 16, 25, 36, 49])