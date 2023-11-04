class Solution(object):
    def getLastMoment(self, n, left, right):
        """
        :type n: int
        :type left: List[int]
        :type right: List[int]
        :rtype: int
        """
        ans=0
        for i in left:
            ans=max(ans,i)
        for j in right:
            ans=max(ans,n-j)
        return ans
        
