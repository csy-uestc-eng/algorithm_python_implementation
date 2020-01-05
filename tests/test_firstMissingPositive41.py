# -*- coding: utf-8 -*-
from unittest import TestCase
from FirstMissingPositive41 import Solution


class TestfirstMissingPositive(TestCase):
    def test_firstMissingPositive(self):
        # 区间无合并
        self.assertEqual(1, Solution().firstMissingPositive([3, 5]))

    def test_firstMissingPositive01(self):
        # 单区间右扩张
        self.assertEqual(4, Solution().firstMissingPositive([1, 2, 3]))

    def test_firstMissingPositive02(self):
        # 单区间左扩张
        self.assertEqual(4, Solution().firstMissingPositive([3, 2, 1]))

    def test_firstMissingPositive03(self):
        # 两个区间合并
        self.assertEqual(6, Solution().firstMissingPositive([1, 2, 4, 5, 3]))
