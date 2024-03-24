class UnionFind:
    def __init__(self,n):
        self.root=[i for i in range(n)]
        self.rank=[1 for _ in range(n)]
    def find(self,x):
        return self.root[x]
    def union(self,x,y):
        rootx=self.find(x)
        rooty=self.find(y)
        if rootx!=rooty:
            for i in range(len(self.root)):
                if self.root[i]==rooty:
                    self.root[i]=rootx
    def isconnected(self,x,y):
        return self.find(x)==self.find(y)
    def noofRoots(self):
        return len(set(self.root))
class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        uf=UnionFind(n)
        logs=sorted(logs,key=lambda x:x[0])
        for t,s,d in logs:
            uf.union(s,d)
            if uf.noofRoots()==1:
                return t
        return -1
