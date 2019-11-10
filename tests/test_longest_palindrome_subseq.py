from unittest import TestCase
from longestPalindromeSubseq import Solution

class TestSolution(TestCase):
    def test_longestPalindromeSubseq(self):
        self.assertEqual(2, Solution().longestPalindromeSubseq('aa'))

    def test_longestPalindromeSubseq01(self):
        self.assertEqual(1, Solution().longestPalindromeSubseq('a'))

    def test_longestPalindromeSubseq02(self):
        self.assertEqual(3, Solution().longestPalindromeSubseq('aba'))

    def test_longestPalindromeSubseq03(self):
        self.assertEqual(9, Solution().longestPalindromeSubseq(
            'a1b2c3d4dcba'))

    def test_longestPalindromeSubseq011(self):
        self.assertEqual(2, Solution().longestPalindromeSubseq01('aa'))

    def test_longestPalindromeSubseq012(self):
        self.assertEqual(1, Solution().longestPalindromeSubseq01('a'))

    def test_longestPalindromeSubseq013(self):
        self.assertEqual(3, Solution().longestPalindromeSubseq01('aba'))

    def test_longestPalindromeSubseq014(self):
        self.assertEqual(9, Solution().longestPalindromeSubseq01(
            'a1b2c3d4dcba'))
