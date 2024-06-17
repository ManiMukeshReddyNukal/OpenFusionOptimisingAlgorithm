class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        m=len(grid)
        n=len(grid[0])
        max_count=0
        row_sum=0
        col_sum=[0]*n
        for i in range(m):
            for j in range(n):
                if j==0 or grid[i][j-1]=="W":
                    row_sum=0
                    for k in range(j,n):
                        if grid[i][k]=="W":
                            break
                        elif grid[i][k]=="E":
                            row_sum+=1
                if i==0 or grid[i-1][j]=="W":
                    col_sum[j]=0
                    for k in range(i,m):
                        if grid[k][j]=="W":
                            break
                        elif grid[k][j]=="E":
                            col_sum[j]+=1
                if grid[i][j]=="0":
                    total_hits=row_sum+col_sum[j]
                    max_count=max(max_count,total_hits)
        return max_count
