class Solution(object):
    def __init__(self):
        self.m = None
        self.n = None

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m = len(grid)
        if m <= 0:
            return 0
        n = len(grid[0])
        self.m = m
        self.n = n
        visited = [[False] * n for j in range(m)]
        cnt = 0
        for i in range(m):
            for j in range(n):
                if not visited[i][j] and grid[i][j] == '1':
                    self.dfs_visit(i, j, grid, visited)
                    cnt += 1
        return cnt

    def adj(self, x, y, g, visited):
        next_node = []
        if x - 1 >= 0 and g[x - 1][y] == '1' and visited[x - 1][y] == False:
            next_node.append((x - 1, y))
        if x + 1 <= self.m - 1 and g[x + 1][y] == '1' and visited[x + 1][
            y] == False:
            next_node.append((x + 1, y))
        if y - 1 >= 0 and g[x][y - 1] == '1' and visited[x][y - 1] == False:
            next_node.append((x, y - 1))
        if y + 1 <= self.n - 1 and g[x][y + 1] == '1' and visited[x][
            y + 1] == False:
            next_node.append((x, y + 1))
        return next_node

    def dfs_visit(self, x, y, g, visited):
        visited[x][y] = True
        for xi, yi in self.adj(x, y, g, visited):
            self.dfs_visit(xi, yi, g, visited)
