class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        @cache
        def rec(amount):
            if amount==0:
                return 0
            if amount<0:
                return float('inf')
            return min((rec(amount-coin) for coin in coins if coin<=amount),default=float('inf'))+1
        res=rec(amount)
        return res if res!=float('inf') else -1
