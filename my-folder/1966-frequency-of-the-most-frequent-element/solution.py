class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        mf=0
        i=j=0
        n=len(nums)
        total=0
        while j<n:
            total+=nums[j]
            while nums[j]*(j-i+1)>total+k:
                total-=nums[i]
                i+=1
            mf=max(mf,j-i+1)
            j+=1
        return mf
