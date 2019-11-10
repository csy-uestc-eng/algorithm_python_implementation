from unittest import TestCase
from kmp import kmp

class TestKmp(TestCase):
    def test_compute_prefix(self):
        self.assertEqual([0, 0, 0, 1, 2, 3, 0, 1],
                         kmp().compute_prefix('ababaca'))

    def test_compute_prefix01(self):
        self.assertEqual([0, 0, 1],
                         kmp().compute_prefix('aa'))

    def test_compute_prefix02(self):
        self.assertEqual([0, 0, 1, 2],
                         kmp().compute_prefix('aaa'))

    def test_match(self):

        self.assertEqual([0, 2, 7], kmp().match('abab', 'abababaabab'))
