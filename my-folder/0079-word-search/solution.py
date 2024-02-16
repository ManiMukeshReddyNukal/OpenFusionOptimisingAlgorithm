class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m=len(board)
        n=len(board[0])
        path=set()
        def dfs(x,y,i):
            if i==len(word):
                return True
            if x<0 or x>=m or y<0 or y>=n or board[x][y]!=word[i] or (x,y) in path:
                return False
            path.add((x,y))
            res= dfs(x+1,y,i+1) or dfs(x-1,y,i+1) or dfs(x,y+1,i+1) or dfs(x,y-1,i+1)
            path.remove((x,y))
            return res
        for i in range(m):
            for j in range(n):
                if dfs(i,j,0):
                    return True
        return False
