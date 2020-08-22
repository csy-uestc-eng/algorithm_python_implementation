# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from functools import lru_cache
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0:
            return list()

    def dfs(self, left, right):

