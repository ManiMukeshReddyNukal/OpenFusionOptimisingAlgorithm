class Solution {
    public int minDifference(int[] nums) {
        int numsize=nums.length;
        if (numsize<4) return 0;
        Arrays.sort(nums);
        int minDifference = Integer.MAX_VALUE;
        for ( int left=0, right=numsize-4; left<4; left++,right++)
        {
            minDifference=Math.min(minDifference, nums[right]-nums[left]);
        }
        return minDifference;
    }
}
