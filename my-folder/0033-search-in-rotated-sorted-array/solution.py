class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(left,right):
            mid=(left+right)//2
            if nums[mid]==target:
                return mid
            if left>right:
                return -1
            if nums[mid]>=nums[left]:
                if nums[mid]>target>=nums[left]:
                    return binary_search(left,mid-1)
                else:
                    return binary_search(mid+1,right)
            else:
                if nums[mid]<target<=nums[right]:
                    return binary_search(mid+1,right)
                else:
                    return binary_search(left,mid-1)    
        return binary_search(0,len(nums)-1)
