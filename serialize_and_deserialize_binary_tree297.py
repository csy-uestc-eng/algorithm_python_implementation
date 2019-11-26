from binary_tree import TreeNode
import json
from Queue import Queue


def build_binary_tree(array):

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


def level_order(root):
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


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        return json.dumps(level_order(root))

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        datas = json.loads(data)
        return build_binary_tree(datas)
