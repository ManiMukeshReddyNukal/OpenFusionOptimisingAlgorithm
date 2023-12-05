class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums=sorted(nums)
        def findsum(num,i,ot):
            j=len(num)-1
            k=i+1
            while k<j:
                if num[k]+num[j]+num[i]==0:
                    if [num[i],num[k],num[j]] not in ot:
                        ot.append([num[i],num[k],num[j]])
                    k+=1
                if num[k]+num[j]+num[i]>0:
                    j-=1
                if num[k]+num[j]+num[i]<0:
                    k+=1
        ot=[]
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i==0 or nums[i-1]!=nums[i]:
                findsum(nums,i,ot)
        return ot
        
