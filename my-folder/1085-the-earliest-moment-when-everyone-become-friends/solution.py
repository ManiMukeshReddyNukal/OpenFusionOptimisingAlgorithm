class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]

    def find(self, x):
        return self.root[x]
		
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            for i in range(len(self.root)):
                if self.root[i] == rootY:
                    self.root[i] = rootX

    def connected(self, x, y):
        return self.find(x) == self.find(y)
    def noOfRoots(self):
        return len(set(self.root))

class Solution(object):
    
    def earliestAcq(self, logs, n):
        """
        :type logs: List[List[int]]
        :type n: int
        :rtype: int
        """
        tree=UnionFind(n)
        logs=sorted(logs, key=lambda x: x[0])
        for log in logs:
            tree.union(log[1],log[2])
            if tree.noOfRoots() == 1:
                return log[0]
        return -1
        
                
        
        
