class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n=len(s)
        countA,countB=collections.Counter(s[:n//2]),collections.Counter(s[n//2:])
        a,b=0,0
        l=['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        for c in l:
            a+=countA[c]
            b+=countB[c]
        return a==b
        
