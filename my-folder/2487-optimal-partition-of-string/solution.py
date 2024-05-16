class Solution:
    def partitionString(self, s: str) -> int:
        distinct=set()
        l,r=0,0
        count=1
        distinct.add(s[0])
        for r in range(1,len(s)):
            if s[r] in distinct:
                distinct=set()
                distinct.add(s[r])
                l=r
                count+=1
            else:
                distinct.add(s[r])
        return count
