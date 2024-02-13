class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k,count=1,1
        n=len(nums)
        for i in range(1,n):
            if nums[i-1]!=nums[i]:
               count=1
               nums[k]=nums[i]
               k+=1
            else:
                count+=1
                if count<=2:
                    nums[k]=nums[i]
                    k+=1
        return k
                    
                    
