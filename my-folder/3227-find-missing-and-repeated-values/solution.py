class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        n=len(grid)
        out=[0]*2
        counter=[0]*n*n
        def findXIndex(val):
            return val/n
        def findYIndex(val):
            return val%n
        for i in range(n):
            for j in range(n):
                counter[grid[i][j]-1]+=1
        out[0]=counter.index(2)+1
        out[1]=counter.index(0)+1
        return out
