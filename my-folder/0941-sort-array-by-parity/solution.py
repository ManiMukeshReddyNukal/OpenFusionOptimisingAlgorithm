class Solution(object):
    def sortArrayByParity(self, nums):
        out=[0]*len(nums)
        print(out)
        l=0
        m=len(nums)-1
        for i in range(len(nums)):
            if nums[i]%2==0 :
                out[l]=nums[i]
                l=l+1
            else :
                out[m]=nums[i]
                m=m-1
        return out            
        
