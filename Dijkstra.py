# -*- coding: utf-8
import sys
from heapq import heapify, heappop


class Node(object):
    def __init__(self, value, cur_distance):
        self.value = value
        self.cur_dis = cur_distance

    def __lt__(self, other):
        return self.cur_dis <= other.cur_dis


def dijkstra(g, s):
    # 复杂度： O(V^2 + E) 。复杂度过低，需要自己实现堆-> O(V + E)
    # node_map存了结点标识到堆中节点元素的映射。
    # 初始化首节点
    node_map = {}
    start = Node(s, 0)
    node_map[s] = start

    # 堆，以距离s的当前距离作关键字建堆
    heap_nodes = [start]
    parent = {}
    for i in g.keys():
        parent[i] = None
        if i != s:
            node = Node(i, sys.maxint)
            heap_nodes.append(node)
            node_map[i] = node
    heapify(heap_nodes)

    visited = []
    while len(heap_nodes) != 0:
        u = heappop(heap_nodes)
        visited.append((u.value, u.cur_dis))
        for v, w in g[u.value].items():
            if node_map[v].cur_dis > node_map[u.value].cur_dis + w:
                node_map[v].cur_dis = node_map[u.value].cur_dis + w
                parent[v] = u.value
        # O(n)
        heapify(heap_nodes)
    return visited

# 有向图的表示：
# g = {
#     'node0': {'adj1': 1, 'adj2': 2}
# }