class Solution:
    dir=[(0,1),(1,0),(-1,0),(0,-1)]
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n=len(grid)
        multi_source_q=deque()
        for i in range(n):
            for j in range(n):
                if grid[i][j]==1:
                    multi_source_q.append((i,j))
                    grid[i][j]=0
                else:
                    grid[i][j]=-1
        while multi_source_q:
            size=len(multi_source_q)
            while size>0:
                curr=multi_source_q.popleft()
                for d in self.dir:
                    di,dj=curr[0]+d[0],curr[1]+d[1]
                    if self.isValidCell(grid, di, dj) and grid[di][dj]==-1:
                        val=grid[curr[0]][curr[1]]
                        grid[di][dj]=val+1
                        multi_source_q.append((di,dj))
                size-=1
        # binary search 
        start,end,res=0,0,-1
        for i in range(n):
            for j in range(n):
                end=max(end,grid[i][j])
        while start<=end:
            mid=start + (end-start)//2
            # do binary
            if self.isValidSafety(grid, mid):
                res=mid
                start=mid+1
            else:
                end=mid-1
        return res
    def isValidCell(self,grid,i,j):
        n=len(grid)
        if i>-1 and i<n and j>-1 and j<n:
            return True
        return False
    def isValidSafety(self,grid,min_safeness):
        n=len(grid)
        if grid[0][0]<min_safeness or grid[-1][-1]<min_safeness:
            return False
        traverseq=deque()
        traverseq.append((0,0))
        visited=set()
        visited.add((0,0))
        while traverseq:
            cur=traverseq.popleft()
            if cur[0]==n-1 and cur[1]==n-1:
                return True
            for d in self.dir:
                di,dj=cur[0]+d[0],cur[1]+d[1]
                if self.isValidCell(grid, di, dj) and (di,dj) not in visited and grid[di][dj]>=min_safeness:
                    visited.add((di,dj))
                    traverseq.append((di,dj))
        return False

