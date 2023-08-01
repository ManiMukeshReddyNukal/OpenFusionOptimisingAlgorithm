class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        if nums[0] > nums[1]:
            return 0
        if nums[len(nums)-1] > nums[len(nums)-2]:
            return len(nums)-1
        i=1
        j=len(nums)-2
        while i<=j:
            mid=i+(j-i)//2
            if nums[mid] > nums[mid + 1] and nums[mid] > nums[mid-1]:
                return mid
            elif nums[mid-1] < nums[mid]:
                i=mid+1
            else:
                j=mid-1
        return None
