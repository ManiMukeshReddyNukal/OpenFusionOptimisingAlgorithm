class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count=Counter()
        l,mx=0,0
        for r,c in enumerate(s):
            count[c]+=1
            mx=max(mx, count[c])
            if r-l+1-mx>k:
                count[s[l]]-=1
                l+=1
        return len(s)-l
