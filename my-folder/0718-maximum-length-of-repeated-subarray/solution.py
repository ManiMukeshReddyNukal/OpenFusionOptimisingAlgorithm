class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        # Initialize the memoization matrix
        memo = [[0] * (len(nums2) + 1) for _ in range(len(nums1) + 1)]
        
        # Iterate over nums1 and nums2 in reverse order
        for i in range(len(nums1) - 1, -1, -1):
            for j in range(len(nums2) - 1, -1, -1):
                if nums1[i] == nums2[j]:
                    # Update the memo matrix if there's a match
                    memo[i][j] = memo[i+1][j+1] + 1
        
        # Find and return the maximum length of the common subarray
        return max(max(row) for row in memo)
