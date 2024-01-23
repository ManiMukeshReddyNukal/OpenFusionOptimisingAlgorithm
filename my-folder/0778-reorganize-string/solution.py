class Solution:
    def reorganizeString(self, s: str) -> str:
        count=Counter(s)
        n=len(s)
        if max(count.values())>(len(s)+1)//2:
            return ""
        out=[""]*n
        idx=0
        counter = sorted(count.items(), key=lambda x: x[1], reverse=True)

        for c,v in counter:
            while v>0:
                    out[idx]=c
                    idx+=2
                    if idx>=n:
                        idx=1
                    v-=1
        return "".join(out)
                
