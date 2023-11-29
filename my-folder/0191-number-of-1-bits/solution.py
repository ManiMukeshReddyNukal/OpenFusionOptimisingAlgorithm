class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count=0
        while n>0:
            i=n%2
            if (i & 1) !=0:
                count+=1
            n=n//2     
        return count
        
