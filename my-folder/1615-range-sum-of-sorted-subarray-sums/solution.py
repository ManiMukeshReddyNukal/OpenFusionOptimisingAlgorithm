class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        arr=[]
        MOD=10**9+7
        left-=1
        right-=1
        for i in range(n):
            currentsum=0
            for j in range(i,n):
                currentsum=(currentsum+nums[j])%MOD
                arr.append(currentsum)
        arr.sort()
        return sum(arr[left:right+1])%MOD
