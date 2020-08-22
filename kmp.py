class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        return self.kmp(haystack, needle)

    def kmp(self, haystack, needle):
        """ kmp 构造 next数组解法
        """
        if not needle:
            return 0
        needle_len = len(needle)
        next_ = self.compute_next(needle)
        matched_len = 0
        for i in range(len(haystack)):
            while matched_len > 0 and haystack[i] != needle[matched_len]:
                matched_len = next_[matched_len - 1]
            if haystack[i] == needle[matched_len]:
                matched_len += 1
            if matched_len == len(needle):
                return i - needle_len + 1
        return -1

    def compute_next(self, needle):
        needle_len = len(needle)
        # next[i]表示needle中[0:i]区间内的字符串最长后缀和最长前缀相等的长度
        # 比如needle = 'ababa'则 next_为： 0, 0, 1, 2, 3.
        next_ = [0] * needle_len
        # matched_len代表当前已经匹配了的长度
        # 计算next.因为next[0]一定为0，故从1开始
        matched_len = 0
        for cur_index in range(1, needle_len):
            while matched_len > 0 and needle[cur_index] != needle[matched_len]:
                # matched_len代表已经匹配的长度，这里减1是因为next数组下标从0开始
                matched_len = next_[matched_len - 1]
            if needle[cur_index] == needle[matched_len]:
                matched_len += 1
            next_[cur_index] = matched_len
        return next_
