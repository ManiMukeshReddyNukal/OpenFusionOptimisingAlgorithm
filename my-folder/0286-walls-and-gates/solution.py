class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        q=[]
        visited=set()
        n=len(rooms)
        m=len(rooms[0])
        for i in range(n):
            for j in range(m):
                if rooms[i][j]==0:
                    q.append((i,j))
                    visited.add((i,j))
        dist=0
        while q:
            for _ in range(len(q)):
                x,y=q.pop(0)
                rooms[x][y]=dist
                for dx,dy in [(1,0),(0,1),(-1,0),(0,-1)]:
                    nx,ny=x+dx,y+dy
                    if 0<=nx<n and 0<=ny<m and (nx,ny) not in visited and rooms[nx][ny]!=-1:
                        q.append((nx,ny))
                        visited.add((nx,ny))
            dist+=1
