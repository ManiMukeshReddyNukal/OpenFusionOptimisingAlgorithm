class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # Get matrix dimensions
        m = len(matrix)
        n = len(matrix[0])
        
        # Initialize the in-degree matrix
        indeg = [[0] * n for _ in range(m)]
        
        # Directions for moving (down, right, up, left)
        dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        
        # Calculate in-degrees
        for i in range(m):
            for j in range(n):
                for (dx, dy) in dir:
                    nx, ny = i + dx, j + dy
                    if 0 <= nx < m and 0 <= ny < n and matrix[nx][ny] < matrix[i][j]:
                        indeg[i][j] += 1
        
        # Initialize the queue with cells that have 0 in-degree
        q = deque()
        for i in range(m):
            for j in range(n):
                if indeg[i][j] == 0:
                    q.append((i, j, 0))  # (row, col, depth)
        
        # Variable to track the maximum depth
        maxdepth = 0
        
        # BFS loop
        while q:
            x, y, depth = q.popleft()
            maxdepth = depth
            for (dx, dy) in dir:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and matrix[nx][ny] > matrix[x][y]:
                    indeg[nx][ny] -= 1
                    if indeg[nx][ny] == 0:
                        q.append((nx, ny, depth + 1))
        
        # Return the length of the longest path
        return maxdepth + 1

