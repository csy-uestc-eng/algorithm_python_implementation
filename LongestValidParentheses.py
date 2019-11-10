
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        if length < 2:
            return 0
        max_cnts = [[0] * (length + 1) for i in range(length+1)]
        for i in range(length, 0, -1):
            for j in range(i + 1, length + 1):
                if s[i - 1] == ')':
                    max_cnts[i][j] = max_cnts[i + 1][j]
                elif s[j-1] == '(':
                    max_cnts[i][j] = max_cnts[i][j - 1]
                elif i + 1 == j:
                    max_cnts[i][j] = 2
                elif max_cnts[i + 1][j - 1] == j - 1 - i:
                    max_cnts[i][j] = j - i + 1
                else:
                    for k in range(i, j):
                        value = max_cnts[i][k] + max_cnts[k+1][j]
                        if value == j - i + 1:
                            max_cnts[i][j] = j - i + 1
                            break
                        else:
                            local_max = max(max_cnts[i][k], max_cnts[k+1][j])
                            max_cnts[i][j] = max(max_cnts[i][j], local_max)
        return max_cnts[1][length]

