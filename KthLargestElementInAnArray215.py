# -*- coding: utf-8 -*-
"""
using min heap to find k largest element.
"""


class MinHeap(object):
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


def findKlargest(array, k):
    """ 堆实现

    使用一个小顶堆，堆大小为k.。遍历完所有元素后，取堆顶元素即是第k.
    注：
        1. 原数组顺序会被改变。
        2. 原数组会在开始增加一个元素。仅用作标记。不使用。
    time complexity: O(nlogk)
    :param array:
    :param k:
    :return:
    """
    min_heap = MinHeap()
    min_heap.build_min_heap(array, k)
    for i in range(k+1, len(array)):
        if array[i] > array[1]:
            array[1], array[i] = array[i], array[1]
            min_heap.min_heapify(array, k, 1)
    return array[1]


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # AC time: 64ms
        # Ac memory: 12.3MB
        return findKlargest(nums, k)