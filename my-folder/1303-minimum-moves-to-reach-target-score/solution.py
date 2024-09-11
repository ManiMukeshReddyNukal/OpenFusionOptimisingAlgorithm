class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        steps=0
        while target>1:
            if target%2==0 and maxDoubles>0:
                while maxDoubles>0 and target>1 and target%2==0:
                    maxDoubles-=1
                    target=target//2
                    steps+=1
            elif maxDoubles==0:
                return steps+target-1
            else:
                target-=1
                steps+=1
        return steps
