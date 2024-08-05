import java.util.*;

class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> resp = new ArrayList<>();
        
        // Step 1: Sort the array to make it easier to avoid duplicates
        Arrays.sort(nums);
        
        // Step 2: Iterate over the array, considering each number as a potential first number of a triplet
        for (int i = 0; i < nums.length; i++) {
            // Skip if the number is greater than 0, as it can't form a zero-sum triplet with positive numbers
            // Skip duplicate elements to avoid duplicate triplets
            if (nums[i] > 0) break;  // Since the array is sorted, no need to continue if the current number is > 0
            if (i == 0 || nums[i] != nums[i - 1]) {
                // Step 3: Find pairs that sum to -nums[i]
                twoSum(nums, i, resp);
            }
        }
        return resp;
    }

    private void twoSum(int[] nums, int i, List<List<Integer>> resp) {
        Set<Integer> mp = new HashSet<>();
        int target = -nums[i];  // The target two numbers need to sum up to

        // Step 4: Iterate over the array starting from i+1 to find pairs
        for (int j = i + 1; j < nums.length; j++) {
            int complement = target - nums[j];
            
            // If the complement exists in the set, we found a valid triplet
            if (mp.contains(complement)) {
                // Add the found triplet to the result list
                resp.add(Arrays.asList(nums[i], nums[j], complement));
                
                // Skip duplicates for the second number
                while (j + 1 < nums.length && nums[j] == nums[j + 1]) j++;
            }
            
            // Add the current number to the set for future complement checks
            mp.add(nums[j]);
        }
    }
}

