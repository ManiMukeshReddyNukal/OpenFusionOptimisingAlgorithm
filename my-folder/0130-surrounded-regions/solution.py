class Solution:
    def solve(self, a: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(a)
        n = len(a[0])
        nodesToVis = [(i,j) for i in range(m) for j in [0,n-1] if a[i][j]=='O'] + [(i,j) for i in [0,m-1] for j in range(n) if a[i][j]=='O']

        for i,j in nodesToVis:
            if a[i][j]=='Y': continue
            st = [(i,j)]
            a[i][j] = 'Y'
            while st:
                curi,curj = st.pop()
                for ni, nj in [(curi+1,curj),(curi-1,curj),(curi,curj+1),(curi,curj-1)]:
                    if 0<=ni<m and 0<=nj<n and a[ni][nj]=='O':
                        a[ni][nj]='Y'
                        st.append((ni,nj))
        for i in range(m):
            for j in range(n):
                if a[i][j]=='O':a[i][j]='X'
        
        for i in range(m):
            for j in range(n):
                if a[i][j]=='Y':a[i][j]='O'


