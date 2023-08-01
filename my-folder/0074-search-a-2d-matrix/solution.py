class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        i=0
        r=m*n-1
        while i <=r:
            mid = i+ (r-i)//2
            midx=mid//n
            midy=mid%n
            if target==matrix[midx][midy]:
                return True
            elif matrix[midx][midy] < target :
                i=mid+1
            else:
                r=mid-1
        return False
             
