from unittest import TestCase
from DecodeWays import Solution

class TestSolution(TestCase):
    def test_numDecodings(self):
        self.assertEqual(3, Solution().numDecodings('122'))

    def test_numDecodings01(self):
        self.assertEqual(3, Solution().numDecodings('222'))

    def test_numDecodings02(self):
        self.assertEqual(1, Solution().numDecodings('2'))

    def test_numDecodings03(self):
        self.assertEqual(1, Solution().numDecodings('34'))

    def test_numDecodings04(self):
        self.assertEqual(0, Solution().numDecodings('0'))

    def test_numDecodings05(self):
        self.assertEqual(1, Solution().numDecodings('10'))

    def test_numDecodings06(self):
        self.assertEqual(1, Solution().numDecodings('120'))

    def test_numDecodings07(self):
        self.assertEqual(2, Solution().numDecodings('227'))
