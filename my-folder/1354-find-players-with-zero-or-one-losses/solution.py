class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        out=[set(),set()]
        s=set()
        for a,b in matches:
            if b in out[1]:
                out[1].remove(b)
                s.add(b)
            elif b not in s:
                out[1].add(b)
            if b in out[0]:
                out[0].remove(b)   
            if a not in out[0] and a not in s and a not in out[1] :
                out[0].add(a)
        out[0]=sorted(list(out[0]))
        out[1]=sorted(list(out[1]))
        return out
