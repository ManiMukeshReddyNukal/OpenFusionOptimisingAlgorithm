class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m=len(grid)
        n=len(grid[0])
        dir = ((1,0),(0,1),(-1,0),(0,-1))
        island=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]=="1":
                    island+=1
                    # write bfs code here 
                    grid[i][j]="0"
                    q=deque()
                    q.append((i,j))
                    while q:
                        a,b=q.popleft()
                        for k,l in (dir):
                            x,y=a+k,b+l
                            if 0<=x<m and 0<=y<n and grid[x][y]=="1":
                                grid[x][y]="0"
                                q.append((x,y))
        return island
                    
