from collections import deque
class Solution:
    def orangesRotting(self, a: List[List[int]]) -> int:
        m = len(a)
        n = len(a[0])
        numor = 0
        rotor = deque()
        time = 0
        for i in range(m):
            for j in range(n):
                if a[i][j]==2: rotor.append((i,j,0))
                if a[i][j]!=0: numor += 1
        
        while rotor:
            curi,curj,curtime = rotor.popleft()
            if curtime>time: time = curtime
            numor-=1
            for ni,nj in [(curi+1,curj),(curi-1,curj),(curi,curj+1),(curi,curj-1)]:
                if 0<=ni<m and 0<=nj<n and a[ni][nj]==1:
                    rotor.append((ni,nj,curtime+1))
                    a[ni][nj]=2
        
        return time if numor==0 else -1
