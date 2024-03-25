class UnionFind:
    def __init__(self,n):
        self.root=[i for i in range(n+1)]
        self.rank=[0 for _ in range(n+1)]
    def find(self,x):
        if x!=self.root[x]:
            self.root[x]=self.find(self.root[x])
        return self.root[x]
    def union(self,x,y):
        rootx=self.find(x)
        rooty=self.find(y)
        if rootx==rooty:
            return False
        else:
            if self.rank[rootx]>self.rank[rooty]:
                self.root[rooty]=rootx
            elif self.rank[rootx]<self.rank[rooty]:
                self.root[rootx]=rooty
            else:
                self.root[rooty]=rootx
                rootx+=1
            return True
    def isconnected(self,x,y):
        return self.find(x)==self.find(y)


class Solution:
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:
        edges=[]
        tcost=0
        for i,w in enumerate(wells):
            edges.append([w,0,i+1])
        for h1,h2,c1 in pipes:
            edges.append([c1,h1,h2])
            edges.append([c1,h2,h1])
        edges.sort(key=lambda x:x[0])
        uf=UnionFind(n)
        for cost,house1,house2 in edges:
            if uf.union(house1,house2):
                tcost+=cost
        return tcost
