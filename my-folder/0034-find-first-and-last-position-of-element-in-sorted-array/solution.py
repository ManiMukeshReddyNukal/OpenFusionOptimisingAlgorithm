class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binarysearch(left,right,bias):
            i=-1
            while left<=right:
                mid=(left+right)//2
                if nums[mid]<target:
                    left=mid+1
                elif nums[mid]>target:
                    right=mid-1
                else:
                    i=mid
                    if bias:
                        right=mid-1
                    else:
                        left=mid+1
            return i
        return [binarysearch(0,len(nums)-1,True),binarysearch(0,len(nums)-1,False)]
