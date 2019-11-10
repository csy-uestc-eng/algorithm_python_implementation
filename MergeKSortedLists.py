# -*- coding: utf-8 -*-

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from Queue import PriorityQueue


# leetcode input ListNode.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# Associate key to Node.
class KeyNode(object):
    def __init__(self, node):
        self.key = node.value
        self.node = node

    def __le__(self, other):
        return self.key < other.key


def merge_k_sorted_list(lists):
    """合并多个有序列表

    :param lists: 多个有序列表。for example:
    [
        [1,4,5],
        [1,3,4],
        [2,6]]
    ]
    :rtype: list. return [1,1,2,3,4,4,5,6]
    """
    k = len(lists)
    # build min heap
    q = PriorityQueue()
    head = ListNode(0)
    pointer = head
    for ele in lists:
        q.put(ele.value, ele)
    while not q.empty():
        value, node = q.get()
        pointer.next = node
        pointer = pointer.next

        next_node = node.next
        if next_node:
            q.put((next_node.value, next_node))
    pointer.next = None
    return head.next


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        return merge_k_sorted_list(lists)
