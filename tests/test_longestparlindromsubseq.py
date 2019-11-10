from unittest import TestCase
from longestPalindromeSubseq import Solution

class TestSolution(TestCase):
    def test_longestPalindrome02(self):
        self.assertEqual(Solution().longestPalindrome02('abccba'), 'abccba')
        
    def test_longestPalindrome02_1(self):
        self.assertEqual(Solution().longestPalindrome02('a'), 'a')
    
    def test_longestPalindrome02_2(self):
        self.assertEqual(Solution().longestPalindrome02('aba'), 'aba')