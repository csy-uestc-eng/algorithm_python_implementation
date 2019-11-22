from unittest import TestCase
from binary_search import binary_search, binary_search_2, binary_search_3


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


class TestBinarySearch03(TestCase):

    def test_binary_search(self):
        arr = [1]
        self.assertEqual(0, binary_search_3(arr, 1))

    def test_binary_search01(self):
        arr = []
        self.assertEqual(0, binary_search_3(arr, 1))

    def test_binary_search02(self):
        arr = [1, 2, 3]
        self.assertEqual(2, binary_search_3(arr, 3))

    def test_binary_search03(self):
        arr = [1, 2, 3, 5]
        self.assertEqual(3, binary_search_3(arr, 4))

    def test_binary_search04(self):
        arr = [1, 2, 3, 4]
        self.assertEqual(4, binary_search_3(arr, 5))

    def test_binary_search05(self):
        arr = [1, 3, 3, 3, 3, 4, 4]
        self.assertEqual(1, binary_search_3(arr, 3))
