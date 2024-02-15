class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        c=0
        for i in range(len(flowerbed)):
            if flowerbed[i]==0:
                emptyleft=(i==0)or (flowerbed[i-1]==0)
                emptyright=(i==len(flowerbed)-1)or (flowerbed[i+1]==0)
                if emptyleft and emptyright:
                    flowerbed[i]=1
                    c+=1
                    if c>=n:
                        return True
        return c>=n
