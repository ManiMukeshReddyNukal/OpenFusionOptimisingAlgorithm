class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans=0
        m=len(grid)
        n=len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j]=="1":
                    q=deque()
                    q.append((i,j))
                    ans+=1
                    self.dfs(q, grid)
        return ans
    def dfs(self,q,grid):
        visited=set()
        dir=[(0,1),(0,-1),(1,0),(-1,0)]
        m=len(grid)
        n=len(grid[0])
        while q:
            (x,y)=q.pop()
            for (dx,dy) in dir:
                nx,ny=x+dx,y+dy
                if (nx,ny) in visited:
                    continue
                if 0<=nx<m and 0<=ny<n and grid[nx][ny]=="1":
                    q.append((nx,ny))
                    grid[nx][ny]="0"
        
