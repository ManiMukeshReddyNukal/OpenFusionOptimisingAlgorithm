from sortedcontainers import SortedList
class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n=len(s)
        pos=[i for i in range(n)]
        def find(x):
            if pos[x]!=x:
                pos[x]=find(pos[x])
            return pos[x]
        for x,y in pairs:
            pos[find(x)]=find(y)
        d=defaultdict(SortedList)
        for i,c in enumerate(s):
            d[find(i)].add(c)
        return "".join(d[find(i)].pop(0) for i in range(n))
