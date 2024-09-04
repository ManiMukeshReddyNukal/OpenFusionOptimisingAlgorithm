class Solution:
    def isValid(self, s: str) -> bool:
        q=[]
        dt={"}":"{",")":"(","]":"["}
        for c in s:
            if c not in dt:
                q.append(c)
            elif q==[] or dt[c]!=q.pop():
                return False
        return q==[]
