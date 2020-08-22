from unittest import TestCase
from strStr_dfa import Solution

class TestSolution(TestCase):
    so = Solution()

    def test_get_dfa(self):
        dp = self.so.get_dfa('ababdababa')
        # X取值依次为[0,0,1,2,0,1,2,3,4]
        for i, e in enumerate(dp):
            for j, number in enumerate(e):
                if number:
                    print(i, chr(j), number)



