from collections import defaultdict


class Solution(object):

    WHITE = 0
    GREY = 1
    BLACK = 2

    def __init__(self):
        self.top_order = list()

    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        colors = {i: Solution.WHITE for i in range(numCourses)}
        g = defaultdict(list)
        for s, e in prerequisites:
            g[s].append(e)

        for v in colors:
            if colors[v] == Solution.WHITE:
                if self.dfs_visit(v, g, colors):
                    return []
        return self.top_order

    def dfs_visit(self, u, g, colors):
        colors[u] = Solution.GREY
        for v in g[u]:
            if colors[v] == Solution.WHITE:
                if self.dfs_visit(v, g, colors):
                    return True
            elif colors[v] == Solution.GREY:
                return True
        colors[u] = Solution.BLACK
        self.top_order.append(u)
        return False
