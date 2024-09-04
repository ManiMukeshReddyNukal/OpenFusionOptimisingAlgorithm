class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m=len(matrix)
        n=len(matrix[0])
        out=[]
        up,left=0,0
        bottom,right=m-1,n-1
        while len(out)<(m*n):
            for col in range(left,right+1):
                out.append(matrix[up][col])
            for row in range(up+1,bottom+1):
                out.append(matrix[row][right])
            if up<bottom:
                for col in range(right-1,left-1,-1):
                    out.append(matrix[bottom][col])
                if left<right:
                    for row in range(bottom-1,up,-1):
                        out.append(matrix[row][left])
            left+=1
            right-=1
            up+=1
            bottom-=1
        return out
