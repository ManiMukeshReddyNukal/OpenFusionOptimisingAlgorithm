class Solution(object):
    def reverseWords(self, s):
        return " ".join(map(lambda word: word[::-1],s.split()))
        
