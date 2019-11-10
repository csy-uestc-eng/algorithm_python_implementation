class kmp(object):
    def match(self, pattern, text):
        prefix = self.compute_prefix(pattern)
        state = 0
        matched_pointer = []
        for i in range(len(text)):
            while state > 0 and text[i] != pattern[state]:
                state = prefix[state]

            if text[i] == pattern[state]:
                state += 1

            if state == len(pattern):
                # matched
                matched_pointer.append(i - state + 1)
                state = prefix[state]
        return matched_pointer

    def compute_prefix(self, _pattern):
        pattern = ' ' + _pattern
        prefix = [0] * len(pattern)
        prefix[1] = 0
        matched_num = 0
        for q in range(2, len(pattern)):
            while (matched_num > 0
                   and pattern[matched_num+1] != pattern[q]):
                matched_num = prefix[matched_num]

            if pattern[matched_num + 1] == pattern[q]:
                matched_num += 1

            prefix[q] = matched_num
        return prefix