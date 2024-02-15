class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        m=len(maze)
        n=len(maze[0])
        visit=[[False]*n for _ in range(m)]
        queue=deque()
        queue.append(start)
        visit[start[0]][start[1]]=True
        d=[(1,0),(-1,0),(0,1),(0,-1)]
        while queue:
            curr=queue.popleft()
            if curr==destination:
                return True
            for (dx,dy) in d:
                x,y=curr[0],curr[1]
                while x>=0 and x<m and y>=0 and y<n and maze[x][y]==0:
                    x+=dx
                    y+=dy
                x-=dx
                y-=dy
                if not visit[x][y]:
                    queue.append([x,y])
                    visit[x][y]=True
        return False
