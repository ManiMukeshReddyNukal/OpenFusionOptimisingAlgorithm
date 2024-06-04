class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        l=0
        uniq=set()
        uniq.add(s[0])
        maxlen=len(uniq)
        for r in range(1,len(s)):
            while s[r] in uniq:
                uniq.remove(s[l])
                l+=1
            uniq.add(s[r])
            maxlen=max(len(uniq),maxlen)
        return maxlen
