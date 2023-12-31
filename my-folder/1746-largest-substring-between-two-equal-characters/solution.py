class Solution(object):
    def maxLengthBetweenEqualCharacters(self, s):
        """
        :type s: str
        :rtype: int
        """
        n=len(s)
        ans=-1
        m={}
        for i in range(n):
            if s[i] in m:
                ans=max(ans,i-m[s[i]]-1)
            else:
                m[s[i]]=i
        return ans
