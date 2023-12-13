class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        l=0
        r=m*n-1
        while l<=r:
            mid=l+(r-l)//2
            midx=mid//n
            midy=mid%n
            if matrix[midx][midy]==target:
                return True
            elif matrix[midx][midy]>target:
                r=mid-1
            else:
                l=mid+1
        return False
             
