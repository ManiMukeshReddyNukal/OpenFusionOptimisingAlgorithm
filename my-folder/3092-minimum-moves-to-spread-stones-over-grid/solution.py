class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        receiver=[]
        giver=[]
        m=len(grid)
        n=len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j]==0:
                    receiver.append((i,j))
                elif grid[i][j]>1:
                    giver.append((i,j,grid[i][j]))
        ans=math.inf
        def backtrack(moves):
            nonlocal receiver
            nonlocal giver
            nonlocal ans
            if len(receiver)==0:
                ans=min(ans,moves)
                return
            receiveri,receiverj=receiver.pop()
            for p in range(len(giver)):
                i,j,k= giver[p]
                if k>1:
                    dist=abs(i-receiveri)+abs(j-receiverj)
                    giver[p]=(i,j,k-1)
                    backtrack(moves+dist)
                giver[p]=(i,j,k)
            receiver.append((receiveri, receiverj))
        backtrack(0)
        return ans
