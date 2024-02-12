class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dir=[(1,0),(0,1),(-1,0),(0,-1)]
        island=0
        m=len(grid)
        n=len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j]=="1":
                    island+=1
                    q=collections.deque()
                    q.append((i,j))
                    while q:
                        k,l=q.popleft()
                        for p,r in dir:
                            modi=k+p
                            modj=l+r
                            if modi>=0 and modj>=0 and modi<m and modj<n and grid[modi][modj]=="1":
                                grid[modi][modj]="0"
                                q.append((modi,modj))
        return island
