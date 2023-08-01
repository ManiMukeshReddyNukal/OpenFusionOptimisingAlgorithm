class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = len(nums)
        if l==1:
            return nums[0]
        if l>1 and nums[0] > nums[1]:
            return nums[1]
        elif l>1 and nums[l-2] > nums[l-1]:
            return nums[l-1]

        i = 0
        r = l - 1
        while i <= r:
            mid = i + (r - i) // 2
            if nums[mid] < nums[mid - 1]:
                return nums[mid]
            elif nums[mid + 1] < nums[mid]:
                return nums[mid + 1]
            elif nums[mid] > nums[r]:  # The pivot point is in the right half
                i = mid + 1
            else:  # The pivot point is in the left half
                r = mid - 1

  # If the loop is not terminated early, the pivot must be at index i


