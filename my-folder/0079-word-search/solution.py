class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n=len(word)
        bn=len(board)
        bm=len(board[0])
        visited=set()
        def dfs(x,y,i):
            if i==n:
                return True
            if x<0 or x>=bn or y<0 or y>=bm or word[i]!=board[x][y] or (x,y) in visited:
                return False
            visited.add((x,y))
            ret=dfs(x+1,y,i+1) or dfs(x,y+1,i+1) or dfs(x,y-1,i+1) or dfs(x-1,y,i+1)
            visited.remove((x,y))
            return ret
        for i in range(bn):
            for j in range(bm):
                if dfs(i,j,0):
                    return True
        return False

