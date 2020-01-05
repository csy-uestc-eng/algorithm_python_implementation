# -*- coding: utf-8 -*-
from Queue import Queue


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


def level_order(root):
    """层序遍历二叉树。

    :param root:
    :return:
    example :
        1
       /\
      2  3
    will return:
    [
     [1],
     [2,3]
    ]
    """
    levels = []
    if not root:
        return []
    cur_level = list()
    cur_level.append(root)
    while len(cur_level) > 0:
        cur_eles = []
        next_level = []
        for node in cur_level:
            cur_eles.append(node.val)
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
        levels.append(cur_eles)
        cur_level = next_level
    return levels


def serialize_binary_tree(root):
    """序列化二叉树

    比如  1
          \
           3
    将序列化为[1, None, 3]
    :param root:
    :return: list
    """
    levels = []
    if not root:
        return []
    cur_level = list()
    cur_level.append(root)
    while any(cur_level):
        next_level = []
        for node in cur_level:
            if node is None:
                levels.append(None)
                continue
            levels.append(node.val)
            if not node.left:
                next_level.append(None)
            else:
                next_level.append(node.left)

            if not node.right:
                next_level.append(None)
            else:
                next_level.append(node.right)
        cur_level = next_level
    return levels

