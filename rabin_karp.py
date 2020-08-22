class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        return self.rabin_karp(haystack, needle)

    def rabin_karp(self, haystack, needle):
        if len(haystack) < len(needle):
            return -1

        alpha_map = {chr(97 + i): i for i in range(26)}

        # 乖积最大数按mod取模，避免溢出
        mod = 2 ** 31

        # 字符串集合，按最小字母计算，最多26个
        N = 26

        L = len(needle)
        needle_hash = 0
        haystack_hash = 0

        for i in range(L):
            needle_hash = (needle_hash * N + alpha_map[needle[i]]) % mod
            haystack_hash = (haystack_hash * N + alpha_map[haystack[i]]) % mod

        nL = pow(N, L, mod)
        for i in range(len(haystack) - L):
            print(needle_hash, haystack_hash)
            if needle_hash == haystack_hash and needle == haystack[i: i + L]:
                return i
            haystack_hash = ((haystack_hash * N - alpha_map[haystack[i]] * nL) + alpha_map[haystack[i + L]]) % mod

        print(needle_hash, haystack_hash)
        if needle_hash == haystack_hash:
            return len(haystack) - L
        return -1