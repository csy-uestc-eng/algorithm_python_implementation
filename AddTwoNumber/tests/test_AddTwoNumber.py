from unittest import TestCase
from AddTwoNumber.AddTwoNumbers import Solution
from AddTwoNumber.AddTwoNumbers import ListNode
class test_AddTwoNumber(TestCase):
    def setUp(self):
        node1 = ListNode(2)
        node2 = ListNode(9)
        node3 = ListNode(9)
        self.l1=node1
        self.l2=node2
        node1.next=node3
    def test_Add(self):
        so = Solution()
        ret = so.addTwoNumbers(self.l1, self.l2)
        while(ret):
            print ret.val
            ret = ret.next
        self.assertTrue(ret)
    def test_copy(self):
        values = {"abc":1}
        val2 = [1,2]
        valdd=(1,2)
        val = values.copy()
        self.modify(val)
        print values["abc"]
    def modify(self, val):
        val["abc"] = 2




