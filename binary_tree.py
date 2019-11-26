# -*- coding: utf-8 -*-
from queue import Queue


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def build_binary_tree(array):
    """从数组构建二叉树

    for example: [1, 2, 4] =>
        1
       / \
      2   4
    使用队列构建
    :param array:
    :return: root
    """
    length = len(array)
    if length == 0:
        return None
    root = TreeNode(array[0])
    q = Queue()
    q.put(root)
    tail = 0
    while not q.empty():
        node = q.get()
        tail += 1
        if tail < length and array[tail] is not None:
            l_node = TreeNode(array[tail])
            node.left = l_node
            q.put(l_node)
        tail += 1
        if tail < length and array[tail] is not None:
            r_node = TreeNode(array[tail])
            node.right = r_node
            q.put(r_node)
    return root


def in_order(root, array):
    if root:
        array.append(root.val)
        in_order(root.left, array)
        in_order(root.right, array)
