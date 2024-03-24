class UnionFind:
    def __init__(self,n):
        self.root=[i for i in range(n)]
        self.rank=[1 for _ in range(n)]
    def find(self,x):
        if x==self.root[x]:
            return x
        self.root[x]=self.find(self.root[x])
        return self.root[x]
    def union(self,x,y):
        rootx=self.find(x)
        rooty=self.find(y)
        if rootx!=rooty:
            if self.rank[rootx]>self.rank[rooty]:
                self.root[rooty]=rootx
            elif self.rank[rootx]<self.rank[rooty]:
                self.root[rootx]=rooty
            else:
                self.root[rooty]=rootx
                self.rank[rootx]+=1
            return True
        else:
            return False
    def isconnected(self,x,y):
        return self.root[x]==self.root[y]
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges)!=n-1:
            return False
        uf=UnionFind(n)
        for s,d in edges:
            if not uf.union(s,d):
                return False
        return True
