class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        k=1
        countof0 = 0
        maxcount = 0
        j=0
        i=0
        n = len(nums)
        while j<n:
            if nums[j]==0:
                countof0 += 1
                while countof0 > k:
                    countof0 -= 1 if nums[i]==0 else 0
                    i += 1
            maxcount = max(maxcount, j-i)
            j+=1
        return maxcount
