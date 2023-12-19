class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        index=((-1,-1),(-1,0),(-1,1),(0,-1),(0,0),(0,1),(1,-1),(1,0),(1,1))
        m=len(img)
        n=len(img[0])
        out=[[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                sum=0
                count=0
                for x,y in index:
                    if 0<=i+x<m and 0<=j+y<n:
                        sum+=img[i+x][j+y]
                        count+=1
                out[i][j]=sum//count
        return out
