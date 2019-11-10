class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def __init__(self):
        self.last_node = ListNode(0)
        self.head = self.last_node

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        while l1 or l2:
            x1 = x2 =0
            if l1:
                x1 = l1.val
                l1 = l1.next
            if l2:
                x2 = l2.val
                l2 = l2.next
            carry, value = divmod(x1 + x2 + carry, 10)
            self.last_node.next = ListNode(value)
            self.last_node = self.last_node.next
        if carry:
            self.last_node.next = ListNode(carry)
            self.last_node = self.last_node.next
        return self.head.next





