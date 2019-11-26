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
        """包含节点root的单边最大路径和。

        比如：
            1
           / \
          2   3
        max_sum(1): 返回4. 即1 + 3
        最大路径和可以看做包括根点的最大路径和以及不包括根结点的。
        该方法将返回包括根结点的最大路径和，
        同时用max_ret 记录当前已遍历结点的最大路径和
        :param root:
        :return:
        """
        if not root.left and not root.right:
            self.max_ret = max(self.max_ret, root.val)
            return root.val
        root_max = root.val
        if root.left:
            left = self.max_sum(root.left)
            root_max = max(root_max, root_max + left)
            self.max_ret = max(max(self.max_ret, left), root_max)

        if root.right:
            right = self.max_sum(root.right)
            # lr 表示根结点 + 左边 + 右边的最大路径和
            lr = root_max + right
            root_max = max(root_max, root.val + right)
            self.max_ret = max(lr,
                               max(self.max_ret, right))

        return root_max
