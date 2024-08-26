class Solution {
    public int maxSubArray(int[] nums) {
        int maxSum = nums[0]; // Initialize with the first element
        int currentSum = nums[0]; // To keep track of the current maximum sum subarray ending at index i
        
        for (int i = 1; i < nums.length; i++) {
            currentSum = Math.max(currentSum + nums[i], nums[i]); // Update the current sum
            maxSum = Math.max(maxSum, currentSum); // Update the maximum sum found so far
        }
        
        return maxSum;
    }
}

