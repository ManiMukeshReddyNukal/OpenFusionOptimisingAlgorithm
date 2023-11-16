class Solution(object):
    def findDifferentBinaryString(self, nums):
        """
        :type nums: List[str]
        :rtype: str
        """
        integers=set()
        for num in nums:
            integers.add(int(num,2))
        n = len(nums)
        for num in range(n+1):
            if num not in integers:
                ans=bin(num)[2:]
                return "0"*(n-len(ans))+ans
        return ""
