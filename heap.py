# -*- coding: utf-8 -*-


class MaxHeap(object):
    def heap_sort(self, elements):
        self.build_max_heap(elements)
        length = len(elements) - 1  # element[0] is useless
        while length >= 2:
            # 这种用法需要再深入了解下
            elements[1], elements[length] = elements[length], elements[1]
            length -= 1
            self.max_heapify(elements, length, 1)
        elements.pop(0)

    def build_max_heap(self, elements):
        length = len(elements)
        elements.insert(0, 0)
        for i in range(length/2, 0, -1):
            self.max_heapify(elements, length, i)

    def max_heapify(self, elements, end, i):
        left = 2 * i
        right = left + 1
        if left <= end and elements[left] > elements[i]:
            largest = left
        else:
            largest = i
        if right <= end and elements[right] > elements[largest]:
            largest = right
        if i != largest:
            elements[i], elements[largest] = elements[largest], elements[i]
            self.max_heapify(elements, end, largest)


class MinHeap(object):
    def heap_sort(self, elements):
        self.build_min_heap(elements)
        length = len(elements) - 1  # element[0] is useless
        while length >= 2:
            # 这种用法需要再深入了解下
            elements[1], elements[length] = elements[length], elements[1]
            length -= 1
            self.min_heapify(elements, length, 1)
        elements.pop(0)

    def build_min_heap(self, elements, length=None):
        if not length:
            length = len(elements)
        elements.insert(0, 0)
        for i in range(length/2, 0, -1):
            self.min_heapify(elements, length, i)

    def min_heapify(self, elements, end, i):
        left = 2 * i
        right = left + 1
        if left <= end and elements[left] < elements[i]:
            least = left
        else:
            least = i
        if right <= end and elements[right] < elements[least]:
            least = right
        if i != least:
            elements[i], elements[least] = elements[least], elements[i]
            self.min_heapify(elements, end, least)