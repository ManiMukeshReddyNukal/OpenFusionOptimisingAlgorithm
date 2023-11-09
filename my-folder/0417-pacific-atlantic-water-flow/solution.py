class Solution(object):
    def pacificAtlantic(self, heights):
        m=len(heights)
        n=len(heights[0])
        pfv=[[False]*n for _ in range(m)]
        atv=[[False]*n for _ in range(m)]
        pfq=deque()
        atq=deque()
        for i in range(n):
            pfq.append((0,i))
            atq.append((m-1,i))
            pfv[0][i]=True
            atv[m-1][i]=True
        for i in range(m):
            pfq.append((i,0))
            atq.append((i,n-1))
            pfv[i][0]=True
            atv[i][n-1]=True
        def bfs(q,v):
            while q:
                x,y=q.popleft()
                v[x][y]=True
                for i,j in [(0,1),(1,0),(-1,0),(0,-1)]:
                    xm,ym=x+i,y+j
                    if 0<=xm<m and 0<=ym<n and not v[xm][ym] and heights[xm][ym] >= heights[x][y]:
                        v[xm][ym]=True
                        q.append((xm,ym))
            return v
        pfv=bfs(pfq,pfv)
        atv=bfs(atq,atv)
        out=[]
        print
        for i in range(m):
            for j in range(n):
                if pfv[i][j] and atv[i][j]:
                    out.append((i,j))
        return out
            
