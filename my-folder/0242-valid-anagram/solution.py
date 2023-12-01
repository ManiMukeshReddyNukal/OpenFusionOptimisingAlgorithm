class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sd={}
        td={}
        for char in s:
            sd[char]=sd.get(char,0)+1
        for char in t:
            td[char]=td.get(char,0)+1
        return sd==td
