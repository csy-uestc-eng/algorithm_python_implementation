from unittest import TestCase
from h_index_ii_0822 import Solution


class TestSolution(TestCase):

    so = Solution()

    def test_hIndex(self):
        self.assertEqual(3, self.so.hIndex([3, 0, 6, 1, 5]))

    def test_hIndex_lower_boundary_one_element(self):
        self.assertEqual(1, self.so.hIndex([3]))
