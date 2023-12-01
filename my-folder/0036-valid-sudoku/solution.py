class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        N=9
        row=[set() for _ in range(N)]
        col=[set() for _ in range(N)]
        box=[set() for _ in range(N)]
        for m in range(N):
            for n in range(N):
                val=board[m][n]
                if val ==".":
                    continue
                if val in row[n]:
                    return False
                row[n].add(val)
                if val in col[m]:
                    return False
                col[m].add(val)
                idx=m//3*3+n//3
                if val in box[idx]:
                    return False
                box[idx].add(val)
        return True
                
