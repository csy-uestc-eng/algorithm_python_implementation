from unittest import TestCase
from leetcode_solution.NumberComplement import Solution as so

class TestNumberComplement(TestCase):
    def setUp(self):
        self.ins = so()
    def test_findComplement(self):
        s = []
        s.append()
        s.pop()
        print s.isalpha()
        print s.isalnum()
        print len(s[3:])
        s.isalpha()

        enc = self.ins.findComplement(5)
        self.assertEquals(enc,2)


