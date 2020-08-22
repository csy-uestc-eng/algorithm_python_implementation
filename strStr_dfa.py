class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        return self.search(haystack, needle)

    def get_dfa(self, pat):
        M = len(pat)
        # dp[状态][字符] = 下个状态
        dp = [[0] * 256 for _ in range(M)]
        # base case
        dp[0][ord(pat[0])] = 1
        # 这里的X即表示的已经匹配的字符串个数。也即当前状态。初始时已经匹配的个数为0
        X = 0
        for j in range(1, M):
            for c in range(0, 256):
                if c == ord(pat[j]):
                    dp[j][c] = j + 1
                else:
                    dp[j][c] = dp[X][c]
            print("X:" + str(X) + "    " + "j:" + str(j) + "pat:" + pat[j])
            X = dp[X][ord(pat[j])]
        return dp

    def search(self, txt, pat):
        if not pat:
            return 0
        if not txt:
            return -1
        M = len(pat)
        N = len(txt)
        dfa = self.get_dfa(pat)
        state = 0
        for j in range(N):
            # 计算 pat 的下一个状态
            state = dfa[state][ord(txt[j])]
            if state == M:
                return j - M + 1
        # 没到达终止态，匹配失败
        return -1
