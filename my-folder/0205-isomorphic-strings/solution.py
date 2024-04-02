class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d=collections.defaultdict()
        d1=collections.defaultdict()
        for i in range(len(s)):
            if s[i] in d:
                if d[s[i]]!=t[i]:
                    return False
            else:
                d[s[i]]=t[i]
            if t[i] in d1:
                if d1[t[i]]!=s[i]:
                    return False
            else:
                d1[t[i]]=s[i]
        return True
