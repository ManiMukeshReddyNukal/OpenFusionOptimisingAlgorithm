class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return matrix
        m,n=len(matrix),len(matrix[0])
        flag1=any(v==0 for v in matrix[0])
        flag2=any(matrix[i][0]==0 for i in range(m))
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j]==0:
                    matrix[i][0]=matrix[0][j]=0
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j]!=0 and ( matrix[i][0]==0 or matrix[0][j]==0):
                    matrix[i][j]=0
        if flag1:
            for i in range(n):
                matrix[0][i]=0
        
        if flag2:
            for i in range(m):
                matrix[i][0]=0
        return matrix
