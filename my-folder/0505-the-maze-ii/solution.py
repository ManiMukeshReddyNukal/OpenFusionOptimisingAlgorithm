import heapq

class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        m, n = len(maze), len(maze[0])
        dist = [[float('inf')] * n for _ in range(m)]
        dist[start[0]][start[1]] = 0
        dire = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        
        def dijkstra():
            pq = []
            heapq.heappush(pq, (0, start[0], start[1]))
            while pq:
                d, x, y = heapq.heappop(pq)
                if [x, y] == destination:
                    return d
                if dist[x][y] < d:
                    continue
                for dx, dy in dire:
                    nx, ny, count = x + dx, y + dy, 0
                    while 0 <= nx < m and 0 <= ny < n and maze[nx][ny] == 0:
                        nx += dx
                        ny += dy
                        count += 1
                    nx -= dx
                    ny -= dy
                    if d + count < dist[nx][ny]:
                        dist[nx][ny] = d + count
                        heapq.heappush(pq, (dist[nx][ny], nx, ny))
        
        dijkstra()
        return dist[destination[0]][destination[1]] if dist[destination[0]][destination[1]] != float('inf') else -1

