from unittest import TestCase
from binary_search import binary_search, binary_search_2


class TestBinarySearch(TestCase):

    @staticmethod
    def func():
        return binary_search

    def test_binary_search(self):
        arr = [1]
        self.assertEqual(0, self.func()(arr, 1))

    def test_binary_search01(self):
        arr = []
        self.assertEqual(-1, self.func()(arr, 1))

    def test_binary_search02(self):
        arr = [1, 2, 3]
        self.assertEqual(2, self.func()(arr, 3))

    def test_binary_search03(self):
        arr = [1, 2, 3, 5]
        self.assertEqual(-1, self.func()(arr, 4))


class TestBinarySearch02(TestBinarySearch):

    @staticmethod
    def func():
        return binary_search_2

