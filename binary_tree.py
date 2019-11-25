# -*- coding: utf-8 -*-


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def build_binary_tree(array, i):
    """从位置i构建树， 返回根结点

    :param array:
    :param i:
    :return:
    """
    length = len(array)
    if i >= length:
        return None
    if array[i] is None:
        return None
    root = TreeNode(array[i])
    left = build_binary_tree(array, 2*i + 1)
    right = build_binary_tree(array, 2*i + 2)
    root.left = left
    root.right = right
    return root


def build_binary_tree01(array):
    """从位置i构建树， 返回根结点

    :param array:
    :param i:
    :return:
    """
    length = len(array)
    if length == 0:
        return None
    root = TreeNode(array[0])
    stack = [root]
    i = 0
    while len(stack) != 0:
        node = stack.pop()
        i = 2*i + 1
        if i < length:
            if array[i]:
                l_node = TreeNode(array[i])
                node.left = l_node
                stack.append(l_node)
        i += 1
        if i < length:
            if array[i]:
                r_node = TreeNode(array[i])
                node.right = r_node
                stack.append(r_node)
    return root


def in_order(root, array):
    if root:
        array.append(root.val)
        in_order(root.left, array)
        in_order(root.right, array)
