# -*- coding: utf-8 -*-

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 前序遍历，结果按从小到大即可。


import sys


class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        previous = [-sys.maxint]
        return self.pre_order(root, previous)

    def pre_order(self, root, previous):
        if root:
            if not self.pre_order(root.left, previous):
                return False
            if root.val <= previous[0]:
                return False
            previous[0] = root.val
            return self.pre_order(root.right, previous)

        return True
