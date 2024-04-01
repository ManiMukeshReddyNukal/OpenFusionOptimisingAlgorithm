from collections import deque
from typing import List  # This is for type hinting

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        n, m = len(grid), len(grid[0])
        q = deque([(0, 0, k, 0)])  # Starting position with (x, y, remaining obstacles, distance)
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        visited = set([(0, 0, k)])

        while q:
            x, y, curr_k, dist = q.popleft()
            if x == n - 1 and y == m - 1:
                return dist  # Reached destination
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m:
                    next_state = (nx, ny, curr_k - grid[nx][ny])
                    if grid[nx][ny] == 1 and curr_k > 0 and next_state not in visited:
                        q.append((*next_state, dist + 1))
                        visited.add(next_state)
                    elif grid[nx][ny] == 0 and next_state not in visited:
                        q.append((*next_state, dist + 1))
                        visited.add(next_state)

        return -1  # No path found

