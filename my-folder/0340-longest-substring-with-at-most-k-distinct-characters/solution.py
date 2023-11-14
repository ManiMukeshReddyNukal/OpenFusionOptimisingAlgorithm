class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
# sliding window
        n=len(s)
        counter=collections.Counter()
        max_len=0
        left=0
        for right in range(n):
            counter[s[right]]+=1
            while(len(counter))>k:
                counter[s[left]]-=1
                if counter[s[left]]==0:
                    del counter[s[left]]
                left+=1
            max_len=max(max_len,right-left+1)
        return max_len


