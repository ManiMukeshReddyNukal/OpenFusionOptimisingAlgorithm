class Solution(object):
    def getnext(self,n):
        s=0
        while n>0:
            d=n%10
            n=n/10
            s+=d**2
        return s
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        s=set()
        while n!=1 and  n not in s:
            s.add(n)
            n=self.getnext(n)
        return n==1
    
        
