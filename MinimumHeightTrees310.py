class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # 当前实现较为优雅，
        # 用了defaultdict库，避免空判断。
        # 用集合作为元素邻接点。增加、删除，求长度操作方便
        if n < 2:
            return 0
        g = collections.defaultdict(set)
        for edge in edges:
            g[edges[0]].add(edges[1])
            g[edges[1]].add(edges[0])

        cur_level = list()
        for e in g:
            if len(g[e]) == 1:
                stack.append(e)
        next_level = list()
        while n > 2:
            for e in cur_level:
                g[e]

