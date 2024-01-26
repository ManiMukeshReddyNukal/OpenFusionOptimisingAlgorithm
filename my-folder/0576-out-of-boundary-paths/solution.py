class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        d={}
        MOD = 10**9 + 7
        def calculate(maxMove,x,y):
            if min(m-x,n-y,x+1,y+1)>maxMove:
                d[x*10000+y*100+maxMove]=0
                return 0
            if x*10000+y*100+maxMove in d:
                return d[x*10000+y*100+maxMove]
            if x<0 or x>=m or y<0 or y>=n:
                d[x*10000+y*100+maxMove]=1
                return 1
            if maxMove==0:
                d[x*10000+y*100+maxMove]=0
                return 0
            d[x*10000+y*100+maxMove]=(calculate(maxMove-1,x+1,y)+calculate(maxMove-1,x-1,y)+calculate(maxMove-1,x,y+1)+calculate(maxMove-1,x,y-1)) % MOD
            return d[x*10000+y*100+maxMove]
        return calculate(maxMove,startRow,startColumn)
        
        
