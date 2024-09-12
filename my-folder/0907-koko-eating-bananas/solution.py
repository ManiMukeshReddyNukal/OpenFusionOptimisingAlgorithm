class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        n=len(piles)
        maxspeed=max(piles)
        minspeed=1
        while minspeed<=maxspeed:
            midspeed=(minspeed+maxspeed)//2
            timespent=0
            for p in piles:
                timespent+=(p//midspeed)+1 if p%midspeed>0 else p//midspeed
            if timespent>h:
                minspeed=midspeed+1
            else:
                maxspeed=midspeed-1
        return minspeed
