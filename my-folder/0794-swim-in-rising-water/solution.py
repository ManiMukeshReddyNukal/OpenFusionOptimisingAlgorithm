class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n=len(grid)
        visited=set()
        minheap=[[grid[0][0],0,0]]
        visited.add((0,0))
        dir=[(1,0),(0,1),(-1,0),(0,-1)]
        while minheap:
            t,x,y=heapq.heappop(minheap)
            if x==n-1 and y==n-1:
                return t
            for (dx,dy) in dir:
                nx,ny=x+dx,y+dy
                if 0<=nx<n and 0<=ny<n and (nx,ny) not in visited:
                    visited.add((nx,ny))
                    heapq.heappush(minheap, (max(t,grid[nx][ny]),nx,ny))
        return -1
