class Solution(object):
    def countPalindromicSubsequence(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans=0
        unq=set(s)
        for l in unq:
            diff=set()
            i,j=s.index(l),s.rindex(l)
            for p in range(i+1,j):
                diff.add(s[p])
            ans+=len(diff)
        return ans
