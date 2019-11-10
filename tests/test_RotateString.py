from unittest import TestCase
from leetcode_solution.RotateString import Solution as so

class TestRotateString(TestCase):
    def setUp(self):
        self.ins = so()
    def test_rotate(self):
        result = self.ins.rotateString01("bqqutquvbtgouklsayfvzewpnrbwfcdmwctusunasdbpbmhnvy" , "wpnrbwfcdmwctusunasdbpbmhnvybqqutquvbtgouklsayfvze")
        self.assertEquals(result, True)
        result = self.ins.rotateString01(None, '')
        self.assertEquals(result, False)
        result = self.ins.rotateString01('', '')
        self.assertEquals(result, True)
        result = self.ins.rotateString01("a", "a")
        self.assertEquals(result, True)
