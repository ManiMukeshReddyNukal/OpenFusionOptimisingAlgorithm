from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0  # The only element is the peak
        if nums[0] > nums[1]:
            return 0  # The first element is a peak
        if nums[n - 1] > nums[n - 2]:
            return n - 1  # The last element is a peak
        
        l, r = 0, n - 1
        while l <= r:
            mid = (l + r) // 2
            if mid > 0 and nums[mid] > nums[mid - 1] and mid < n - 1 and nums[mid] > nums[mid + 1]:
                return mid  # Mid is a peak
            elif mid > 0 and nums[mid - 1] > nums[mid]:
                r = mid - 1  # Peak is to the left
            else:
                l = mid + 1  # Peak is to the right
        
        # This return statement is a fallback and theoretically should never be reached because
        # the while loop should always return from inside. 
        return l

