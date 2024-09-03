class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        maxlen=1
        left=0
        uniq=set()
        for right in range(len(s)):
            while s[right] in uniq:
                uniq.remove(s[left])
                left+=1
            uniq.add(s[right])
            maxlen=max(len(uniq),maxlen)
        return maxlen
