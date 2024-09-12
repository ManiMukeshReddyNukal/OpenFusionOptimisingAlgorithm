class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binarysearch(left,right):
            mid=(left+right)//2
            if nums[mid]==target:
                return mid
            if left>right:
                return -1
            if nums[mid]>=nums[left]:
                if nums[mid]>=target>=nums[left]:
                    return binarysearch(left, mid-1)
                else:
                    return binarysearch(mid+1, right)
            else:
                if nums[mid]<=target<=nums[right]:
                    return binarysearch(mid+1, right)
                else:
                    return binarysearch(left, mid-1)
        return binarysearch(0, len(nums)-1)
