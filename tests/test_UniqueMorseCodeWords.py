from unittest import TestCase
from leetcode_solution.UniqueMorseCodeWords import Solution as so

class TestUniqueMorseCodeWords(TestCase):
    def setUp(self):
        self.ins = so()
    def test_encode(self):
        enc = self.ins.encode("ab")
        self.assertEquals(enc,'.--...')
        enc = self.ins.encode("")
        self.assertEquals(enc,'')
    def test_uniqueMorseRepresentations(self):
        words = ["gin", "zen", "gig", "msg"]
        self.assertEquals(2,self.ins.uniqueMorseRepresentations(words))
        self.assertEquals(0,self.ins.uniqueMorseRepresentations(""))

