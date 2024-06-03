class Solution:
    def dfs(self,q,grid):
        dir=[(1,0),(-1,0),(0,1),(0,-1)]
        visited=set()
        m=len(grid)
        n=len(grid[0])
        while q:
            (x,y)=q.pop()
            visited.add((x,y))
            for (i,j) in dir:
                mx,my=x+i,y+j
                if (mx,my) in visited:
                    continue
                if 0<=mx<m and 0<=my<n and grid[mx][my]=="1":
                    q.append((mx,my))
                    grid[mx][my]=0
    def numIslands(self, grid: List[List[str]]) -> int:
        islands=0
        m=len(grid)
        n=len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j]=="1":
                    q=deque()
                    islands+=1
                    q.append((i,j))
                    self.dfs(q,grid)
        return islands
