class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if k==0:
            return 0
        distinct=defaultdict(int)
        n=len(s)
        l=0
        ans=0
        for r in range(n):
            distinct[s[r]]+=1
            while len(distinct.keys())>k:
                distinct[s[l]]-=1
                if distinct[s[l]]<=0:
                    del distinct[s[l]]
                l+=1  
            ans=max(r-l+1,ans)
        return ans
