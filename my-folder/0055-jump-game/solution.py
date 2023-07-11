class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxreachableposition=nums[0]
        i=1
        while i<len(nums) and i<=maxreachableposition:
            maxreachableposition=max(maxreachableposition,i+nums[i])
            i+=1
        if(maxreachableposition>=len(nums)-1):
            return True
        else:
            return False


