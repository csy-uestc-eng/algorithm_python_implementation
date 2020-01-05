from unittest import TestCase
from binary_tree import build_binary_tree, in_order, level_order


class TestBinaryTree(TestCase):
    @staticmethod
    def list_equal(l1, l2):
        if len(l1) != len(l2):
            return False
        for i in range(len(l1)):
            if isinstance(l1[i], list):
                if not TestBinaryTree.list_equal(l1[i], l2[i]):
                    return False
            elif l1[i] != l2[i]:
                return False
        return True

    def test_build_binary_tree(self):
        array = [-10, 9, 20, None, None, 15, 7]
        root = build_binary_tree(array)
        in_order_array = []
        in_order(root, in_order_array)
        array.remove(None)
        self.assertEqual(self.list_equal(
            [-10, 9, 20, 15, 7], in_order_array), True)

    def test_build_binary_tree02(self):
        array = [5, 4, 8, 11, None,
                 13, 4, 7, 2, None,
                 None, None, 1]
        root = build_binary_tree(array)
        in_order_array = []
        in_order(root, in_order_array)
        array.remove(None)
        self.assertEqual(self.list_equal(
            [5, 4, 11, 7, 2, 8, 13, 4, 1], in_order_array), True)

    def test_level_order(self):
        array = [5, 4, 8]
        root = build_binary_tree(array)
        self.assertEqual(
            self.list_equal(
                [[5], [4, 8]],
                level_order(root)),
            True)

    def test_level_order01(self):
        array = [5, 4, 8, 1]
        root = build_binary_tree(array)
        self.assertEqual(
            self.list_equal(
                [[5], [4, 8], [1]],
                level_order(root)),
            True)

