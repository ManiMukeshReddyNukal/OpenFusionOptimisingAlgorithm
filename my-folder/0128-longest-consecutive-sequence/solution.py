class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        ans = 0
        for i in s:
            if i-1 not in s:
                y = i+1
                while y in s:
                    y += 1
                ans = max(ans, y-i)
        return ans
