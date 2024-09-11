class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        f=grid[0]
        for row in range(1,m):
            temp=[math.inf]*n
            for i in range(n):
                for j in range(n):
                    temp[j]=min(temp[j], moveCost[grid[row-1][i]][j]+f[i]+grid[row][j])
            f=temp
        return min(f)
