class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowdict=defaultdict(set)
        coldict=defaultdict(set)
        boxdict=defaultdict(set)
        n=len(board)
        m=len(board[0])
        for i in range(n):
            for j in range(m):
                if board[i][j]!=".":
                    boxno=(i//3)*3+(j//3)
                    if board[i][j] in rowdict[i] or board[i][j] in coldict[j] or board[i][j] in boxdict[boxno]:
                        return False
                    rowdict[i].add(board[i][j])
                    coldict[j].add(board[i][j])
                    boxdict[boxno].add(board[i][j])
        return True

