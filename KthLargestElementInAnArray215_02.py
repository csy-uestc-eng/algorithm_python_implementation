# -*- coding: utf-8 -*-
import random


def partition(array, s, e, pivot_pos=None):
    """
    partition过程：
    1.将参考值 pivot放到最右边
    2.pos记录的位置表示在pos左边的值全小于pivot_value.
    3.最后将pos和参考值（最右边的元素）交换。
    :param array:
    :param s: 开始元素
    :param e: 结束元素
    :param pivot_pos: 参考元素的位置。若不传。则在[s, e]中随机选
    :return:
    """
    if s == e:
        return s
    if pivot_pos is None:
        pivot_pos = random.randint(s, e)
    pivot_value = array[pivot_pos]
    array[e], array[pivot_pos] = array[pivot_pos], array[e]
    pos = s
    for i in range(s, e + 1):
        if array[i] < pivot_value:
            array[i], array[pos] = array[pos], array[i]
            pos += 1
    array[pos], array[e] = array[e], array[pos]
    return pos


def find_k_least(array, k):
    """分治 + 快排思想

     找第k小的的元素，则寻找从小到大排序后数据中第k 个元素(0 < k < n-1)
     选择一个数x,将比x小的放左边，大的放右边
     比如 3, 2, 4, 5. 若 k= 2， x= 3。
     则有  2, 3, 4, 5。。。 此时 pos[x] = 1 < 2 。则找递归寻找findkMinist([4, 5], 1)
    :param array:
    :param k: 表示array中第k小的数。 1<= k <= len(array)
    :return:
        未发现时返回None. 发现后返回第k小的数。
    """
    n = len(array)
    if n <= 0 or k > n or k <= 0:
        return None
    pos = partition(array, 0, len(array) - 1)
    if pos + 1 == k:
        return array[pos]
    elif pos + 1 < k:
        return find_k_least(array[pos+1:], k - pos - 1)
    else:
        return find_k_least(array[:pos], k)


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # 执行用时:72ms, 在所有python提交中击败了68.11 % 的用户
        # 内存消耗:12.2MB, 在所有python提交中击败了44.49 % 的用户
        return find_k_least(nums, len(nums) - k + 1)
