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
        len_s, len_p = len(s), len(p)
        


class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
