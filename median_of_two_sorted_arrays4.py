def find_k_minist(l1, s, e, l2, s2, e2, k):
    if s > e:
        return find_k_minist_one(l2, s2, e2, k)
    elif s2 > e2:
        return find_k_minist_one(l1, s, e, k)
    l_cnt = (e - s)/2 + 1
    r_cnt = (e2 - s2)/2 + 1
    l_mid = l1[s + l_cnt - 1]
    r_mid = l2[s2 + r_cnt - 1]
    if k == 1:
        return min(l_mid, r_mid)
    elif k == l_cnt + r_cnt:
        return max(l_mid, r_mid)
    elif k > l_cnt + r_cnt:
        return find_k_minist(l1, s + l_cnt, e,
                             l2, s2 + r_cnt, e2,
                             k - l_cnt - r_cnt)
    elif k < l_cnt + r_cnt:
        return find_k_minist(l1, s, s + l_cnt - 1, l2, s2, s2 + r_cnt - 1, k)
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

def find_k_minist_one(l, s, e, k):
    cnt = (e - s)/2 + 1
    mid = s + cnt - 1
    if k == mid:
        return l[mid]
    elif k < mid:
        return find_k_minist_one(l, s, s + cnt - 1, k)
    mid = n // 2

    if alist[mid - 1] < item <= alist[mid]:
        return mid
    elif item <= alist[mid - 1]:
        return binary_search_3(alist[:mid - 1], item)

    else:
        return find_k_minist_one(l, s + cnt, e, k - cnt)
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
        nums1.insert(0, -1)
        nums2.insert(0, -1)
        length = len(nums1) + len(nums2)

        if length % 2 == 0:
            l = find_k_minist(nums1, 1, len(nums1) - 1,
                              nums2, 1, len(nums2) - 1,
                              (length - 2) / 2)
            r = find_k_minist(nums1, 1, len(nums1) - 1,
                              nums2, 1, len(nums2) - 1,
                              (length - 2) / 2 + 1)
            return (l + r) / 2.0

        return find_k_minist(nums1, 1, len(nums1) - 1,
                             nums2, 1, len(nums2) - 1,
                             (length - 2) / 2 + 1)
        cnt = len(nums1) + len(nums2)
        if cnt % 2 == 1:
            return find_k_minist_of_two_sorted_array(nums1, nums2, cnt // 2 + 1)
        else:
            l = find_k_minist_of_two_sorted_array(nums1, nums2, cnt // 2)
            r = find_k_minist_of_two_sorted_array(nums1, nums2, cnt//2 + 1)
            return (l+r) / 2.0
