class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        count=0
        remaining=0
        sx,sy=0,0
        for i in range(m):
            for j in range(n):
                if grid[i][j]>=0:
                    remaining+=1
                if grid[i][j]==1:
                    sx,sy=i,j
        d=[(1,0),(-1,0),(0,1),(0,-1)]
        def backtrack(x,y,remain):
            temp=grid[x][y]
            nonlocal count
            if grid[x][y]==2 and remain==1:
                count+=1
                return
            grid[x][y]=-4
            remain-=1
            for (dx,dy) in d:
                nx,ny=dx+x,dy+y
                if nx<0 or nx>=m or ny<0 or ny>=n:
                    continue
                if grid[nx][ny]<0:
                    continue
                backtrack(nx,ny,remain)
            grid[x][y]=temp
        backtrack(sx,sy,remaining)
        return count
        
            

