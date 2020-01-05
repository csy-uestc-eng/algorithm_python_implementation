from unittest import TestCase
from median_of_two_sorted_arrays4 import Solution


class TestSolution(TestCase):
    def test_findMedianSortedArrays(self):
        self.assertEqual(3, Solution().findMedianSortedArrays(
            [1], [2, 3, 4, 5]))

    def test_findMedianSortedArrays01(self):
        self.assertEqual(1.5, Solution().findMedianSortedArrays(
            [1], [2]))

    def test_findMedianSortedArrays02(self):
        self.assertEqual(2, Solution().findMedianSortedArrays(
            [], [2]))

    def test_findMedianSortedArrays03(self):
        self.assertEqual(2.5, Solution().findMedianSortedArrays(
            [], [2, 3]))

    def test_findMedianSortedArrays04(self):
        self.assertEqual(-1, Solution().findMedianSortedArrays(
            [3], [-2, -1]))
