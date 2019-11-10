from unittest import TestCase
from MedianFinding import split, findkMinist, findKlargest


class TestSplit(TestCase):
    def list_ele_equal(self, lista, listb):
        if len(lista) != len(listb):
            return False
        for i in range(len(lista)):
            if lista[i] != listb[i]:
                return False
        return True

    def test_split_noele(self):
        array = []
        split(array, 0, 0)
        self.assertEqual(1, 1)

    def test_split_one_ele(self):
        array = [1]
        split(array, 0, 0)
        self.assertEqual(array[0], 1)

    def test_split_two_ele(self):
        array = [2, 1]
        split(array, 0, 1)
        self.assertEqual(self.list_ele_equal(array, [1, 2]), True)

    def test_split_range(self):
        array = [2, 1, 1, 3]
        split(array, 0, 1)
        self.assertEqual(self.list_ele_equal(array, [1, 2, 1, 3]), True)

    def test_split_range01(self):
        array = [3, 2, 3, 1, 2]
        split(array, 0, len(array) - 1, pivot_pos=0)
        self.assertEqual(self.list_ele_equal(array, [2, 2, 1, 3, 3]), True)

    def test_split_normal(self):
        array = [2, 1, 1, 3]
        split(array, 0, 3, pivot_pos=0)
        self.assertEqual(self.list_ele_equal(array, [1, 1, 2, 3]), True)

    def test_findkminiest(self):
        self.assertEqual(findkMinist([1], 1), 1)

    def test_findkminiest_outofrange(self):
        self.assertEqual(findkMinist([1], 2), None)

    def test_findkminiest_max(self):
        array = [1, 2, 3, 4, 5]
        self.assertEqual(findkMinist(array, len(array)), 5)

    def test_findkminiest_min(self):
        array = [1, 2, 3, 4, 5]
        self.assertEqual(findkMinist(array, 1), 1)

    def test_findkminiest_random(self):
        array = [2, 1, 3, 5, 4]
        self.assertEqual(findkMinist(array, 4), 4)

    def test_findkminiest_random01(self):
        array = [3, 2, 3, 1, 2, 4, 5, 5, 6]
        self.assertEqual(findkMinist(array, 6), 4)

    def test_findkminiest_random02(self):
        array = [3, 2, 3, 1, 2, 4, 5, 5, 6, 7, 7, 8,
                 2, 3, 1, 1, 1, 10, 11, 5, 6, 2, 4, 7, 8, 5, 6]
        self.assertEqual(findkMinist(array, len(array) - 2 + 1), 10)

    def test_findKlargest(self):
        array = [3, 2, 3, 1, 2, 4, 5, 5, 6, 7, 7, 8,
                 2, 3, 1, 1, 1, 10, 11, 5, 6, 2, 4, 7, 8, 5, 6]
        self.assertEqual(findKlargest(array, 2), 10)
