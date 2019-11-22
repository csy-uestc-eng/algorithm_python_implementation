# -*- coding: utf-8 -*-
def binary_search_3(alist, item):
    """返回alist中小于x的元素个数

    :param alist:
    :param item:
    :return: 0~len(alist)
    """
    n = len(alist)
    if n == 0:
        return 0
    # 提前判断退出，避免后面直接mid-1会导致数组越界
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


def find_k_minist_of_two_sorted_array(arr1, arr2, k):
    """找到排序数据arr1, arr2中第k小的数。

    :param arr1:
    :param arr2:
    :param k: 1 <= k <= len(arr1) + len(arr2)
    :return:
    """
    if len(arr1) == 0 and len(arr2) == 0:
        return 0
    if len(arr1) == 0:
        return arr2[k - 1]
    if len(arr2) == 0:
        return arr1[k - 1]
    mid1 = len(arr1) // 2
    k2 = binary_search_3(arr2, arr1[mid1])
    if mid1 + 1 + k2 == k:
        return arr1[mid1]
    elif mid1 + 1 + k2 > k:
        return find_k_minist_of_two_sorted_array(arr1[:mid1], arr2[:k2], k)
    else:
        return find_k_minist_of_two_sorted_array(
            arr1[mid1 + 1:],
            arr2[k2:],
            k - mid1 - 1 - k2
            )


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        cnt = len(nums1) + len(nums2)
        if cnt % 2 == 1:
            return find_k_minist_of_two_sorted_array(nums1, nums2, cnt // 2 + 1)
        else:
            l = find_k_minist_of_two_sorted_array(nums1, nums2, cnt // 2)
            r = find_k_minist_of_two_sorted_array(nums1, nums2, cnt//2 + 1)
            return (l+r) / 2.0
