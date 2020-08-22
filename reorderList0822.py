# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# *********题目描述******************
# 给定一个单链表 L：L0→L1→…→Ln-1→Ln ，
# 将其重新排列后变为： L0→Ln→L1→Ln-1→L2→Ln-2→…
#
# 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
#
# 示例 1:
#
# 给定链表 1->2->3->4, 重新排列为 1->4->2->3.
# 示例 2:
#
# 给定链表 1->2->3->4->5, 重新排列为 1->5->2->4->3.


class Solution:
    def reorderList(self, head):
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return None
        mid_node = self.find_mid(head)
        new_head = self.reverse_list(mid_node.next)
        mid_node.next = None

        ret = head
        while new_head:
            iter_new_node = new_head
            new_head = new_head.next
            iter_new_node.next = head.next
            head.next = iter_new_node
            head = head.next.next
        return ret

    @staticmethod
    def find_mid(head):
        if not head:
            return None

        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    @staticmethod
    def reverse_list(head):
        if not head:
            return None

        new_head = tail = None
        tail = head
        while tail.next:
            tail = tail.next

        new_head = tail
        while head != new_head:
            tmp_node = head
            head = head.next
            tmp_node.next = new_head.next
            new_head.next = tmp_node

        return new_head




