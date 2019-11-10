# -*- coding: utf-8 -*-
import random
from heap import MinHeap


def swap(array, a, b):
    temp = array[a]
    array[a] = array[b]
    array[b] = temp


def split(array, s, e, pivot_pos=None):
    """
    split过程还很不熟悉。需要复习下。
    1.将参考值 pivot放到最右边
    2.pos记录的位置表示，在pos左边的值全小于pivot_value.
    3。最后将pos和最右边的值 交换。
    :param array:
    :param s:
    :param e:
    :param pivot_pos:
    :return:
    """
    if s == e:
        return s
    if pivot_pos is None:
        pivot_pos = random.randint(s, e)
    pivot_value = array[pivot_pos]
    swap(array, e, pivot_pos)
    pos = s
    for i in range(s, e + 1):
        if array[i] < pivot_value:
            swap(array, i, pos)
            pos += 1
    swap(array, pos, e)
    return pos


def findkMinist(array, k):
    """分治 + 快排思想

     找第k小的的元素，则寻找从小到大排序后数据中第k 个元素(0 < k < n-1)
     选择一个数x,将比x小的放左边，大的放右边
     比如 3, 2, 4, 5. 若 k= 2， x= 3。
     则有  2, 3, 4, 5。。。 此时 pos[x] = 1 < 2 。则找递归寻找findkMinist([4, 5], 1)
    :param array:
    :param k:
    :return:
    """
    n = len(array)
    if n <= 0 or k > n or k <= 0:
        return None
    pos = split(array, 0, len(array) - 1)
    if pos + 1 == k:
        return array[pos]
    elif pos + 1 < k:
        return findkMinist(array[pos+1:], k - pos -1)
    else:
        return findkMinist(array[:pos], k)


def findKlargest(array, k):
    """ 堆实现

    使用一个小顶堆，堆大小为k.。遍历完所有元素后，取堆顶元素即是第k
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

