class Solution(object):
    def largestSubmatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        ans=0
        m=len(matrix)
        n=len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j]!=0 and i>0:
                    matrix[i][j]=matrix[i][j]+matrix[i-1][j]
            curr_row = sorted(matrix[i], reverse=True)
            for i in range(n):
                    ans = max(ans, curr_row[i] * (i + 1))
        return ans
