class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp=0
        minprice=prices[0]
        for price in prices[1:]:
            if minprice<price:
                maxp=max(maxp,price-minprice)
            else:
                minprice=price
        return maxp
