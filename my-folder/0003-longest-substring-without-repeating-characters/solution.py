from collections import Counter
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n=len(s)
        i=0
        j=0
        m=0
        d=collections.defaultdict()
        while j<n:
          d[s[j]]=d.get(s[j],0)+1
          while d[s[j]]>1:
            d[s[i]]-=1
            i+=1
          m=max(m,j-i+1)
          j+=1
        return m
