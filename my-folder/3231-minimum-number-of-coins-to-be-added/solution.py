class Solution:
    def minimumAddedCoins(self, coins: List[int], target: int) -> int:
        maxi=0
        count=0
        coins.sort()
        for coin in coins:
            while maxi+1<coin and maxi<target:
                count+=1
                maxi+=maxi+1
            if maxi>target:
                break
            maxi+=coin
        while maxi<target:
            count+=1
            maxi+=maxi+1
        return count
