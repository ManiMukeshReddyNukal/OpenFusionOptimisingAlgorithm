class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        counter=set()
        if k>len(nums)-1:
            k=len(nums)-1
        for i in range(k+1):
            if nums[i] in counter:
                return True
            counter.add(nums[i])
        for i in range(k+1,len(nums)):
            counter.remove(nums[i-k-1])
            if nums[i] in counter:
                return True
            counter.add(nums[i])
        return False
            
