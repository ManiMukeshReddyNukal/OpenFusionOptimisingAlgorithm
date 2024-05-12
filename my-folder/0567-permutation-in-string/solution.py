class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def dictcont(d2,d1):
            for k,v in d1.items():
                if not(k in d2 and d2[k]>=v):
                    return False
            return True
        
        ds1 = {}
        for c in s1:
            if c not in ds1: ds1[c]=0
            ds1[c] += 1
        
        ds2 = {}
        n=len(s2)
        start = 0
        for i in range(n):
            if s2[i] in ds1:
                if s2[i] not in ds2: ds2[s2[i]] = 0
                ds2[s2[i]] += 1
                # print(ds1)
                # print(ds2)
                # print(dictcont(ds1,ds2))
                while not dictcont(ds1,ds2):
                    ds2[s2[start]]-=1
                    if ds2[s2[start]]==0: del ds2[s2[start]]
                    start+=1
                # print(start,i)
                if dictcont(ds2,ds1): return True
            else:
                ds2 = {}
                start = i+1
        return False
