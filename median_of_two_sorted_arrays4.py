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


def find_k_minist_one(l, s, e, k):
    cnt = (e - s)/2 + 1
    mid = s + cnt - 1
    if k == cnt:
        return l[mid]
    elif k < cnt:
        return find_k_minist_one(l, s, s + cnt - 1, k)
    else:
        return find_k_minist_one(l, s + cnt, e, k - cnt)


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
