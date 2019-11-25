from unittest import TestCase
from binary_tree import build_binary_tree, build_binary_tree01
from binary_tree_maximum_path_sum import Solution


class TestSolution(TestCase):
    def test_maxPathSum(self):
        root = build_binary_tree([-10, 9, 20, None, None, 15, 7], 0)
        self.assertEqual(Solution().maxPathSum(root), 42)

    def test_maxPathSum01(self):
        root = build_binary_tree([-2, -1], 0)
        self.assertEqual(Solution().maxPathSum(root), -1)

    def test_maxPathSum02(self):
        root = build_binary_tree([1, -2, -3, 1, 3, -2, None, -1], 0)
        self.assertEqual(Solution().maxPathSum(root), 3)

    def test_maxPathSum03(self):
        root = build_binary_tree01([5, 4, 8, 11, None,
                                   13, 4, 7, 2, None,
                                   None, None, 1])
        self.assertEqual(Solution().maxPathSum(root), 48)

