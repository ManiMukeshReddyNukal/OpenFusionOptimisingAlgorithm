class Solution(object):
    def findDiagonalOrder(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        groups=defaultdict(list)
        for row in range(len(nums)-1,-1,-1):
            for col in range(len(nums[row])):
                diagonal=row+col
                groups[diagonal].append(nums[row][col])
        ans=[]
        curr=0
        while curr in groups:
            ans.extend(groups[curr])
            curr+=1
        return ans
