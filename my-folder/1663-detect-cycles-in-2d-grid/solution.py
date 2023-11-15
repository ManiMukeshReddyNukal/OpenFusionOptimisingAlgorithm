import collections

class Solution(object):
    def containsCycle(self, grid):
        m, n = len(grid), len(grid[0])
        dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def bfs(start_i, start_j, char):
            q = collections.deque()
            q.append((start_i, start_j, None))  # Including parent as None initially
            grid[start_i][start_j] = char.upper()

            while q:
                i, j, parent = q.popleft()
                for di, dj in dir:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < m and 0 <= nj < n:
                        if grid[ni][nj] == char:
                            grid[ni][nj] = char.upper()
                            q.append((ni, nj, (i, j)))
                        elif grid[ni][nj] == char.upper() and (ni, nj) != parent:
                            return True
            return False

        for i in range(m):
            for j in range(n):
                if grid[i][j].islower() and bfs(i, j, grid[i][j]):
                    return True

        return False

