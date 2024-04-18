class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        arr=s.split(" ")
        dit={}
        n=len(arr)
        i=0
        if len(pattern)!=n:
            return False
        for c in pattern:
            if c in dit:
                if dit.get(c)!=arr[i]:
                    return False
            else:
                dit[c]=arr[i]
            i+=1
        if len(set(dit.keys()))!=len(set(dit.values())):
            return False
        return True
