class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        n=len(prices)
        min_pur=prices[0]+prices[1]
        if min_pur<=money:
            return money-min_pur
        else:
            return money
