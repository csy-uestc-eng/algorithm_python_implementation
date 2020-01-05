# -*- coding: utf-8 -*-
from unittest import TestCase
from regular_expression_matching41 import Solution_DP


class TestSolution_DP(TestCase):
    def setUp(self):
        self.obj = Solution_DP()

    def test_isMatch_special(self):
        self.assertEqual(True, self.obj.isMatch('', '*'))

    def test_isMatch_special01(self):
        self.assertEqual(True, self.obj.isMatch('', '.*'))

    def test_isMatch_special02(self):
        self.assertEqual(False, self.obj.isMatch('', '..*'))

    def test_isMatch_special03(self):
        self.assertEqual(True, self.obj.isMatch('', '.*.*'))

    def test_isMatch(self):
        self.assertEqual(True, self.obj.isMatch('ab', 'ab'))

    def test_isMatch_comma(self):
        self.assertEqual(True, self.obj.isMatch('ab', 'a.'))

    def test_isMatch_asterisk(self):
        # 星号0次匹配
        self.assertEqual(True, self.obj.isMatch('a', 'ab*'))

    def test_isMatch_asterisk00(self):
        # 星号1次匹配(遗漏)
        self.assertEqual(True, self.obj.isMatch('aa', 'a*'))

    def test_isMatch_asterisk01(self):
        # 星号多次匹配
        self.assertEqual(True, self.obj.isMatch('abb', 'ab*'))

    def test_isMatch_asterisk02(self):
        # ** 非合法正则
        self.assertEqual(True, self.obj.isMatch('abb', 'ab**'))

    def test_isMatch_asterisk_03(self):
        # *(遗漏)
        self.assertEqual(True, self.obj.isMatch('', 'c*'))

    def test_isMatch_asterisk_04(self):
        # *(遗漏)
        self.assertEqual(True, self.obj.isMatch('ab', 'abc*'))

    def test_isMatch_comma_asterisk(self):
        # .*
        self.assertEqual(True, self.obj.isMatch('ab', 'ab.*'))

    def test_isMatch_comma_asterisk_01(self):
        # .*
        self.assertEqual(True, self.obj.isMatch('abcb', 'ab.*'))

    def test_isMatch_comma_asterisk_02(self):
        # 多个.*
        self.assertEqual(True, self.obj.isMatch('cbab', 'cb.*ab.*'))

    def test_isMatch_comma_asterisk_03(self):
        # 多个.*
        self.assertEqual(True, self.obj.isMatch('miss', 'mis*'))

    def test_isMatch_comma_asterisk_04(self):
        # 多个.*(遗漏)
        self.assertEqual(True, self.obj.isMatch('aa', 'ab*a*'))

    def test_isMatch_comma_asterisk_05(self):
        # 多个.*(遗漏)
        self.assertEqual(True, self.obj.isMatch('a', '.*.*'))

    def test_isMatch_comma_asterisk_06(self):
        # 多个.*(遗漏)
        self.assertEqual(True, self.obj.isMatch('bab', '..*'))

    def test_isMatch_comma_asterisk_07(self):
        # 多个.*(遗漏)
        self.assertEqual(True, self.obj.isMatch('cbbbaccbcacbcca', '.*b*a*.a*b*.a*'))


