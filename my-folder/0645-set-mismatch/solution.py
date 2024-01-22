class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        rep=-1
        mis=-1
        for a in nums:
            if nums[abs(a)-1]<0:
                rep=abs(a)
            else:
                nums[abs(a)-1]=-nums[abs(a)-1]
        for i in range(len(nums)):
            if nums[i]>0:
                mis=i+1
        return [rep,mis]
