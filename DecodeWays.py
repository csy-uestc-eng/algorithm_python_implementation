# -*- coding: utf-8 -*-

import copy
class Solution(object):
    ALPHA = {
        '1': 'A', '2': 'B', '3': 'C', '4': 'D', '5': 'E', '6': 'F',
        '7': 'G', '8': 'H', '9': 'I', '10': 'J', '11': 'K', '12': 'L',
        '13': 'M', '14': 'N', '15': 'O', '16': 'P', '17': 'Q', '18': 'R',
        '19': 'S', '20': 'T', '21': 'U', '22': 'V', '23': 'W', '24': 'X',
        '25': 'Y', '26': 'Z'
    }
    def numDecodings(self, s):
        """
        1.不同子问题解空间存在相同解。针对该题，不同子问题存在相同的切割方案。
        比如122：
            12，2-->[(1,2,2), (12, 2)]
        122
            1，22-->[(1,2,2), (1, 22)]
        这里切割方案1，2 和 2，1就一样的。原因是切割顺序无关。
        2. 未考虑特殊字符0的处理
        3. 时间复杂度超了
        :type s: str
        :rtype: int
        """

        crow = [set() for i in range(len(s) + 1)]
        c = [copy.deepcopy(crow) for i in range(len(s) + 1)]
        for i in range(len(s), 0, -1):
            for j in range(i, len(s) + 1):
                if i == j:
                    if s[i-1] != '0':
                        c[i][j].add(self.ALPHA[s[i-1]])
                elif i + 1 == j:
                    if s[i - 1] != '0' and s[i] != '0':
                        c[i][j].add(self.ALPHA[s[i - 1]] + self.ALPHA[s[i]])
                    if 10 <= int(s[i - 1:j]) <= 26:
                        c[i][j].add(self.ALPHA[s[i - 1:j]])
                else:
                    tmp_set = set()
                    for k in range(i, j):
                        for l_ele in c[i][k]:
                            for r_ele in c[k+1][j]:
                                tmp_set.add(l_ele + r_ele)
                    c[i][j] = tmp_set
        return len(c[1][len(s)])
