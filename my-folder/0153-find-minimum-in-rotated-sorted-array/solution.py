from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        r = n - 1

        while l <= r:
            mid = (l + r) // 2

            if (mid == 0 or nums[mid - 1] > nums[mid]) and (mid == n - 1 or nums[mid] < nums[mid + 1]):
                return nums[mid]

            if nums[mid] < nums[r]:
                r = mid - 1
            else:
                l = mid + 1

        # This should not happen if the array is properly rotated
        return  # Indicate that an error occurred or handle it in a way that makes sense for your use case

