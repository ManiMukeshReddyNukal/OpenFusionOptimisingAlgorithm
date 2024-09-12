class UnionFind:
    def __init__(self, n):
        self.p = list(range(n))
        self.size = [1] * n

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, a, b):
        pa, pb = self.find(a), self.find(b)
        if pa == pb:
            return False
        if self.size[pa] > self.size[pb]:
            self.p[pb] = pa
            self.size[pa] += self.size[pb]
        else:
            self.p[pa] = pb
            self.size[pb] += self.size[pa]
        return True

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        emaildict={}
        uf=UnionFind(len(accounts))
        for i,emails in enumerate(accounts):
            for email in emails[1:]:
                if email in emaildict:
                    idx=emaildict[email]
                    uf.union( i,idx)
                else:
                    emaildict[email]=i
        g=defaultdict(set)
        for i,(_,*email) in enumerate(accounts):
            idx=uf.find(i)
            g[idx].update(email)
        return [[accounts[root][0]]+sorted(emails) for root,emails in g.items()]
