from collections import deque

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        perimeter = 0
        stack = deque()
        
        # Find the first '1' and start from there
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    stack.append((i, j))
                    grid[i][j] = 2  # Mark as visited by changing it to 2
                    break
            if stack:
                break
        
        # Explore the island using BFS
        while stack:
            x, y = stack.popleft()
            # Check all 4 possible directions
            for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                xd, yd = x + dx, y + dy
                # Check if the neighbour is within bounds
                if 0 <= xd < n and 0 <= yd < m:
                    if grid[xd][yd] == 1:
                        stack.append((xd, yd))
                        grid[xd][yd] = 2
                    elif grid[xd][yd] == 0:
                        perimeter += 1  # Water or visited cell contributes to perimeter
                else:
                    perimeter += 1  # Out of bounds contributes to perimeter

        return perimeter

