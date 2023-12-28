class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        @lru_cache(None)
        def dp(i,lastchar,lastcount,k):
            if k<0:
                return float('inf')
            if i==n:
                return 0
            delete_char=dp(i+1,lastchar,lastcount,k-1)
            if s[i]==lastchar:
                keep_char=dp(i + 1, lastchar, lastcount + 1, k) + (lastcount in [1, 9, 99])
            else:
                keep_char=dp(i+1,s[i],1,k)+1
            return min(keep_char,delete_char)
        n=len(s)
        return dp(0,"",0,k)
