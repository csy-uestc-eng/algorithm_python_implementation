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
        self.assertEqual(2, Solution().findMedianSortedArrays(
            [1, 2, 3], []))

    def test_findMedianSortedArrays05(self):
        self.assertEqual(3.5, Solution().findMedianSortedArrays(
            [1, 2, 3], [4, 5, 6]))

    def test_findMedianSortedArrays06(self):
        self.assertEqual(6, Solution().findMedianSortedArrays(
            [8, 9], [1, 2, 3, 6, 8]))
