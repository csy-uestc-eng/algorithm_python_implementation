from unittest import TestCase
from leetcode_solution.LongestValidParentheses import Solution

class TesLlongestValidParenthes(TestCase):
    def test_longestValidParentheses(self):
        self.assertEqual(2, Solution().longestValidParentheses('(()'))

    def test_longestValidParentheses01(self):
        self.assertEqual(4, Solution().longestValidParentheses('()()'))

    def test_longestValidParentheses02(self):
        self.assertEqual(6, Solution().longestValidParentheses('(()())'))

    def test_longestValidParentheses03(self):
        self.assertEqual(2, Solution().longestValidParentheses("()))"))

    def test_longestValidParentheses04(self):
        self.assertEqual(4, Solution().longestValidParentheses("((())(()"))

    def test_longestValidParentheses05(self):
        self.assertEqual(4, Solution().longestValidParentheses(
            ")()(()()(()()(()))((())()()()))((()(())(((()()(((((()))(((()))()())((((()()))))()((())()))))()(((((((()))()(((()()(((()()()())()))(()))()())))))())))))))())))()"))
