# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        row,col=binaryMatrix.dimensions()
        ans=col
        for r in range(row):
            i=bisect_left(range(col), 1, key=lambda x:binaryMatrix.get(r, x))
            ans=min(ans,i)
        return ans if ans<col else -1
