class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n=len(prices)
        if n==0 or n==1:
          return 0
        mi=prices[0]
        ma=prices[1]
        mp=0
        for i in range(1,n):
          mi=min(prices[i],mi)
          mp=max(prices[i]-mi,mp)
        return mp
