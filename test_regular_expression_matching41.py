# -*- coding: utf-8 -*-
from unittest import TestCase
from regular_expression_matching41 import Solution_DP


class TestSolution_DP(TestCase):
    def setUp(self):
        self.obj = Solution_DP()

    def test_isMatch(self):
        self.assertEqual(True, self.obj.isMatch('ab', 'ab'))

    def test_isMatch_comma(self):
        self.assertEqual(True, self.obj.isMatch('ab', 'a.'))

    def test_isMatch_asterisk(self):
        # 星号0次匹配
        self.assertEqual(True, self.obj.isMatch('a', 'ab*'))

    def test_isMatch_asterisk01(self):
        # 星号多次匹配
        self.assertEqual(True, self.obj.isMatch('abb', 'ab*'))

    def test_isMatch_asterisk02(self):
        # ** 非合法正则
        self.assertEqual(True, self.obj.isMatch('abb', 'ab**'))

    def test_isMatch_comma_asterisk(self):
        # .*
        self.assertEqual(True, self.obj.isMatch('ab', 'ab.*'))

    def test_isMatch_comma_asterisk_01(self):
        # .*
        self.assertEqual(True, self.obj.isMatch('abcb', 'ab.*'))

    def test_isMatch_comma_asterisk_02(self):
        # 多个.*
        self.assertEqual(True, self.obj.isMatch('cbab dbab cb', 'cb*.ab.*'))
