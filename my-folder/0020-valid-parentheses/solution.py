class Solution:
    def isValid(self, s: str) -> bool:
        q=[]
        d={"}":"{",")":"(","]":"["}
        for c in s:
            if c not in d:
                q.append(c)
            elif q==[] or d[c]!=q.pop():
                return False       
        return q==[]

