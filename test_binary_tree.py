from unittest import TestCase
from binary_tree import build_binary_tree, in_order


class TestBinaryTree(TestCase):
    @staticmethod
    def list_equal(l1, l2):
        if len(l1) != len(l2):
            return False
        for i in range(len(l1)):
            if l1[i] != l2[i]:
                return False
        return True

    def test_build_binary_tree(self):
        array = [-10, 9, 20, None, None, 15, 7]
        root = build_binary_tree(array, 0)
        in_order_array = []
        in_order(root, in_order_array)
        array.remove(None)
        self.assertEqual(self.list_equal(
            [-10, 9, 20, 15, 7], in_order_array), True)

    def test_build_binary_tree01(self):
        array = [-10, 9, 20, None, None, 15, 7]
        root = build_binary_tree(array, 0)
        in_order_array = []
        in_order(root, in_order_array)
        array.remove(None)
        self.assertEqual(self.list_equal(
            [-10, 9, 20, 15, 7], in_order_array), True)
