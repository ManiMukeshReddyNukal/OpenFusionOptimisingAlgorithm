class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        arr=[i for i in range(1,n+1)]
        startindex=-1
        while len(arr)>1:
            for i in range(k):
                startindex+=1
                if startindex>=len(arr):
                    startindex=0
            arr.pop(startindex)
            startindex-=1
        return arr[0]
