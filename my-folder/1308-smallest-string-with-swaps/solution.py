
from sortedcontainers import SortedList

class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1] * size

    def find(self, x):
        while x != self.root[x]:
            x = self.root[x]
        return x
		
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1

    def connected(self, x, y):
        return self.find(x) == self.find(y)
    
    def getMaxrank():
        maxrank=max(self.rank)
        
    
    
class Solution(object):
    def smallestStringWithSwaps(self, s, pairs):
        """
        :type s: str
        :type pairs: List[List[int]]
        :rtype: str
        """
        t=UnionFind(len(s))
        for pair in pairs:
            t.union(pair[0],pair[1])
        lookup = defaultdict(SortedList)
        for i, node in enumerate(t.root):
            lookup[t.find(node)].add(s[i])
        ans = []
        for i in range(len(s)):
            ans.append(lookup[t.find(i)].pop(0))
        return ''.join(ans)
        
        
