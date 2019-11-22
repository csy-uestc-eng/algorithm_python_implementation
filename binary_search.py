# -*- coding: utf-8 -*-


def binary_search(alist, item):
    """二分查找 非递归方式

    :return -1 if not find.
            index if find.
    """

    n = len(alist)
    start = 0
    end = n - 1
    while start <= end:
        mid = (start + end) // 2
        if alist[mid] == item:
            return mid
        elif item < alist[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return -1


def binary_search_2(alist, item):
    """二分查找 递归方式

    :return -1 if not find.
            index if find.
    """
    n = len(alist)
    if 0 == n:
        return -1
    mid = n // 2
    if alist[mid] == item:
        return mid
    elif item < alist[mid]:
        return binary_search_2(alist[:mid], item)
    else:
        pos = binary_search_2(alist[mid + 1:], item)
        if pos == -1:
            return -1
        return mid + 1 + pos


def binary_search_3(alist, item):
    """返回alist中小于x的元素个数

    :param alist:
    :param item:
    :return: 0~len(alist)
    """
    n = len(alist)
    if n == 0:
        return 0
    if alist[0] >= item:
        return 0
    if alist[n-1] < item:
        return n

    mid = n // 2

    if alist[mid - 1] < item <= alist[mid]:
        return mid
    elif item <= alist[mid - 1]:
        return binary_search_3(alist[:mid - 1], item)
    else:
        return mid + 1 + binary_search_3(alist[mid + 1:], item)
