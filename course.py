# -*- coding: utf-8 -*-
from collections import defaultdict


class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """

        parent = {}
        g = {}
        for i in range(numCourses):
            g[i] = []
        for s, e in prerequisites:
            g[s].append(e)

        for v in range(numCourses):
            if v not in parent:
                parent[v] = None
                if self.dfs_has_cycle(v, g, parent):
                    return False
        return True

    @staticmethod
    def backward_edge(u, v, parent):
        while u is not None:
            if u == v:
                return True
            u = parent[u]
        return False

    def dfs_has_cycle(self, u, g, parent):
        for v in g[u]:
            if v not in parent:
                parent[v] = u
                if self.dfs_has_cycle(v, g, parent):
                    return True
            elif self.backward_edge(u, v, parent):
                return True
        return False


class Node(object):

    WHITE = 0
    GREY = 1
    BLACK = 2

    def __init__(self, value, color):
        self.value = value
        self.color = color
        self.d = None
        self.f = None


class Solution02(object):
    """
    教科书： 深度优先算法
    """
    def __init__(self):
        self.time = 0

    @staticmethod
    def backward_edge(u, v, parent):
        while u is not None:
            if u == v:
                return True
            u = parent[u]
        return False

    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        self.time = 0
        parent = {}
        nodes = {i: Node(i, Node.WHITE) for i in range(numCourses)}
        g = {i: list() for i in range(numCourses)}
        for s, e in prerequisites:
                g[s].append(e)

        for v in nodes:
            if nodes[v].color == Node.WHITE:
                parent[v] = None
                if self.dfs_visit(v, g, parent, nodes):
                    return []
        node_objs = nodes.values()
        node_objs.sort(key=lambda n: n.f)
        return [node.value for node in node_objs]

    def dfs_visit(self, u, g, parent, nodes):
        self.time += 1
        nodes[u].d = self.time
        nodes[u].color = Node.GREY
        for v in g[u]:
            if nodes[v].color == Node.WHITE:
                parent[v] = u
                if self.dfs_visit(v, g, parent, nodes):
                    return True
            elif self.backward_edge(u, v, parent):
                return True
        nodes[u].color = Node.BLACK
        self.time += 1
        nodes[u].f = self.time
        return False
