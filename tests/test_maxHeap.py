from unittest import TestCase
from heap import MaxHeap


class TestMaxHeap(TestCase):
    def list_ele_equal(self, lista, listb):
        if len(lista) != len(listb):
            return False
        for i in range(len(lista)):
            if lista[i] != listb[i]:
                return False
        return True

    def list_is_up(self, elements):
        if len(elements) == 1:
            return True
        for i in range(len(elements) - 2):
            if elements[i] > elements[i+1]:
                return False
        return True

    def test_heap_sort(self):
        elements = [1, 4, 6, 2, 6, 5, 4, 3, 2, 71, 69]
        MaxHeap().heap_sort(elements)
        self.assertEqual(self.list_is_up(elements), True)

    def test_heap_sort_one_ele(self):
        elements = [1]
        MaxHeap().heap_sort(elements)
        self.assertEqual(self.list_is_up(elements), True)
