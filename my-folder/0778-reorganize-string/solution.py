class Solution:
    def reorganizeString(self, s: str) -> str:
        n=len(s)
        count = Counter(s)
        if (max(count.values())>(len(s)+1)//2):
            return ""
        out=[""]*n
        count=sorted(count.items(), key=lambda x:x[1], reverse=True)
        idx=0
        for c,v in count:
            if(v>0):
                for i in range(v):
                    out[idx]=c
                    idx+=2
                    if idx>=n:
                        idx=1
        return "".join(out)
