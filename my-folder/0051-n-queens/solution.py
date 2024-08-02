class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col=set()
        positivediag=set()
        negativediag=set()
        output=[]
        matrix=[["."]*n for _ in range(n)]
        def backtrack(r):
            if r==n:
                cp=["".join(col) for col in matrix]
                output.append(cp)
            for c in range(n):
                if c in col or (r+c) in positivediag or (r-c) in negativediag:
                    continue
                col.add(c)
                positivediag.add(r+c)
                negativediag.add(r-c)
                matrix[r][c]="Q"
                backtrack(r+1)
                col.remove(c)
                positivediag.remove(r+c)
                negativediag.remove(r-c)
                matrix[r][c]="."
        backtrack(0)
        return output
