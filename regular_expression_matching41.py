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
    """DP解法

    """
    def isMatch(self, s, p):
        len_s, len_p = len(s) + 1, len(p) + 1
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
                            # [a-z]*
                            if p[j - 2] != s[i - 1]:
                                # abb,ac*
                                match[i][j] = match[i][j-2]
                            else:
                                # abb,ab* or aa, a*
                                for k in range(i, 0, -1):
                                    if s[k - 1] == p[j - 2]:
                                        # aa, ab*a*
                                        if match[k][j-2]:
                                            match[i][j] = match[k][j-2]
                                            break
                                    else:
                                        match[i][j] = match[k][j-2] or match[i][j]
                                        break
                                if k == 1 and s[0] == p[j - 2] and not match[i][j]:
                                    match[i][j] = match[0][j-2]
                                match[i][j] = match[i][j] or match[i][j - 2]

                        else:
                            # .*
                            if j == 2:
                                match[i][j] = True
                            else:
                                # ab, ab.* or abcb, ab.*
                                for k in range(i, 0, -1):
                                    if s[k - 1] == p[j - 3]:
                                        if match[k][j-2]:
                                            match[i][j] = True
                                            break
                                    else:
                                        match[i][j] = match[i][j] or match[k][j-2]

        return match[len_s - 1][len_p - 1]


class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
