# -*- coding: utf-8 -*-

class DFA:
    alphabets = [chr(p) for p in range(97, 123)]

    @classmethod
    def build(cls, pattern):
        state = 0
        rules = dict()
        pattern = pattern.lstrip('*')
        for seq, p in enumerate(pattern):
            if p == '*':
                if pattern[seq - 1] == '*':
                    continue
                elif pattern[seq - 1] in cls.alphabets:
                    rules[state] = {pattern[seq - 1]: state}
                else:
                    # .*
                    rules[state] = {chr(c): state for c in range(97, 123)}
                    for i in range(seq + 1, len(pattern)):
                        if pattern[i] not in ['.', '*']:
                            rules[state][pattern[i]] = state + 1
                            state += 1
                            break
            elif p == '.':
                rules[state] = {chr(c): state + 1 for c in range(97, 123)}
                state += 1
            if p in cls.alphabets:
                rules[state] = {p: state + 1}
                state += 1
        return 0, state, rules


class Solution_DP(object):
    """DP解法,前缀，太难理解

    """
    def isMatch(self, s, p):
        len_s, len_p = len(s) + 1, len(p) + 1
        # match[i][i]：代表s[0:i-1]与p[0:j-1]是否匹配
        match = [[False] * len_p for i in range(len_s)]
        match[0][0] = True

        # 初始化match[0][j]
        for j in range(1, len_p):
            if p[j - 1] != '*':
                match[0][j] = False
            else:
                if j == 1:
                    match[0][j] = True
                else:
                    match[0][j] = match[0][j-2]

        for i in range(1, len_s):
            for j in range(1, len_p):
                # i, j 代表数组中第i，j个数。数组取时需要-1
                if s[i - 1] == p[j - 1] or p[j - 1] == '.':
                    match[i][j] = match[i - 1][j-1]
                elif p[j - 1] == '*':
                    if j == 1:
                        match[i][j] = match[i][j - 1]
                    else:
                        if p[j - 2] == '*':
                            # **
                            match[i][j] = match[i][j - 1]
                        elif p[j - 2] != '.':
                            # a*
                            # aaa, a*(a*匹配0-n个a)
                            k = i
                            while k > 0:
                                if s[k - 1] == p[j - 2]:
                                    # aa, ab*a*
                                    if match[k][j-2]:
                                        match[i][j] = match[k][j-2]
                                        break
                                else:
                                    break
                                k = k - 1
                            match[i][j] = match[i][j] or match[i][j-2] or match[k][j-2]
                        else:
                            # .*
                            if j == 2:
                                match[i][j] = True
                            else:
                                # ab, ab.* or abcb, ab.*
                                k = i
                                while k > 0:
                                    if s[k - 1] == p[j - 3] or p[j - 3] in ['.', '*']:
                                        if match[k][j-2]:
                                            match[i][j] = True
                                            break
                                    k = k - 1
                                match[i][j] = match[i][j] or match[i][j - 2] or \
                                              match[k][j - 2]

        return match[len_s - 1][len_p - 1]


class Solution_DP01(object):
    """DP解法，后缀

    """
    def isMatch(self, s, p):
        # match[i][i]：代表s[i:]与p[j:]是否匹配
        match = [[False] * (len(p) + 1) for i in range(len(s) + 1)]
        match[-1][-1] = True

        for i in range(len(s), -1, -1):
            for j in range(len(p) - 1, -1, -1):
                first_match = i < len(s) and p[j] in {s[i], '.'}
                if j + 1 < len(p) and p[j + 1] == '*':
                    match[i][j] = match[i][j + 2] or first_match and match[i + 1][j]
                else:
                    match[i][j] = first_match and match[i+1][j+1]

        return match[0][0]

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
