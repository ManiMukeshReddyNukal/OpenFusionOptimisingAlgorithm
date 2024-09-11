from collections import deque
import math

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        def valid(row, col):
            return 0 <= row < m and 0 <= col < n
        
        m = len(mat)
        n = len(mat[0])
        # Initialize the result matrix
        resp = [[math.inf] * n for _ in range(m)]
        seen = set()
        q = deque()
        
        # Add all '0' cells to the queue and mark them seen, also set their resp to 0
        for row in range(m):
            for col in range(n):
                if mat[row][col] == 0:
                    q.append((row, col, 0))  # (row, col, distance)
                    seen.add((row, col))
                    resp[row][col] = 0
        
        # Directions for moving in the grid (right, left, down, up)
        dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        # Perform BFS
        while q:
            x, y, step = q.popleft()
            for dx, dy in dir:
                nx, ny = x + dx, y + dy
                if (nx, ny) not in seen and valid(nx, ny):
                    seen.add((nx, ny))
                    q.append((nx, ny, step + 1))
                    resp[nx][ny] = step + 1
        
        return resp

