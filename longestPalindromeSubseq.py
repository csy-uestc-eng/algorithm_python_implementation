class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) <= 1:
            return len(s)
        lpn = [[0] * len(s) for i in range(len(s))]
        for i in range(len(s) - 1, -1, -1):
            for j in range(i, len(s)):
                if i == j:
                    lpn[i][j] = 1
                else:
                    last_p = s.rfind(s[i], i + 1, j + 1)
                    if last_p == -1:
                        lpn[i][j] = lpn[i + 1][j]
                    else:
                        lpn[i][j] = max(2 + lpn[i + 1][last_p - 1], lpn[i + 1][j])
        return lpn[0][len(s) - 1]

    def longestPalindromeSubseq01(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) <= 1:
            return len(s)
        lpn = [[-1] * len(s) for i in range(len(s))]
        return self.db_up_to_bottom(s, 0, len(s) - 1, lpn)

    def longestPalindrome02(self, s):
        """
        :type s: str
        :rtype: str
        """
        r = [[True] * len(s) for i in range(len(s))]
        start = 0
        length = 0
        if len(s) <= 1:
            return s
        for i in range(len(s) - 1, -1, -1):
            for j in range(i + 1, len(s)):
                if i + 1 == j:
                    r[i][j] = (s[i] == s[j])
                elif s[i] == s[j]:
                    r[i][j] = r[i + 1][j - 1]
                else:
                    r[i][j] = False

                if r[i][j] and j - i + 1 > length:
                    length = j - i + 1
                    start = i
        return s[start: start + length]

    def db_up_to_bottom(self, s, i, j, lpn):
        if lpn[i][j] != -1:
            return lpn[i][j]
        if i > j or len(s) <= 0:
            return 0
        if i == j:
            lpn[i][j] = 1
            return lpn[i][j]
        last_p = s.rfind(s[i], i + 1, j + 1)
        if last_p == -1:
            lpn[i][j] = self.db_up_to_bottom(s, i+1, j, lpn)
        else:
            lpn[i][j] = max(2 + self.db_up_to_bottom(s, i+1, last_p - 1, lpn),
                            self.db_up_to_bottom(s, i + 1, j, lpn))
        return lpn[i][j]