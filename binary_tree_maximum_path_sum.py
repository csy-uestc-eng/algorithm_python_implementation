# -*- coding: utf-8 -*-


class Solution(object):
    def __init__(self):
        self.max_ret = None

    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.max_ret = root.val
        self.max_sum(root)
        return self.max_ret

    def max_sum(self, root):
        """包含节点root的最大路径和。

        :param root:
        :return:
        """
        if not root.left and not root.right:
            self.max_ret = max(self.max_ret, root.val)
            return root.val
        ret = root.val
        cur = root.val
        if root.left:
            left = self.max_sum(root.left)
            ret = max(ret, ret + left)
            cur = ret
            self.max_ret = max(max(self.max_ret, left), ret)

        if root.right:
            right = self.max_sum(root.right)
            ret = max(ret, ret + right)
            cur = max(cur, root.val + right)
            self.max_ret = max(ret, max(self.max_ret, right))

        return cur
