# -*- coding: utf-8 -*-

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        if not graph:
            return True
        colors = [0] * len(graph)
        def dfs(node, parent_color):
            # 判断从当前节点出发是可构成二分图
            if colors[node] != 0:
                return colors[node] != parent_color
            colors[node] = 1 if parent_color == 2 else 2
            for j in range(len(graph[node])):
                if not dfs(graph[node][j], colors[node]):
                    return False
            return True

        for i in range(len(colors)):
            if colors[i] == 0:
                if not dfs(i, 1):
                    return False
        return True