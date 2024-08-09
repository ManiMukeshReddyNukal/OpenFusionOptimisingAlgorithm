class Solution {
    public int longestSubarray(int[] nums, int limit) {
        Deque<Integer> minQ = new LinkedList<>();
        Deque<Integer> maxQ = new LinkedList<>();
        int left=0;
        int ans=0;
        for (int right=0; right<nums.length; right++){
            while (!maxQ.isEmpty() && maxQ.peekLast() <nums[right]) {
                maxQ.pollLast();
            }
            maxQ.offerLast(nums[right]);
            while (!minQ.isEmpty() && minQ.peekLast() >nums[right]) {
                minQ.pollLast();
            }
            minQ.offerLast(nums[right]);

            while(maxQ.peekFirst()-minQ.peekFirst()>limit){
                if(nums[left]==maxQ.peekFirst()){
                    maxQ.pollFirst();
                }
                if(minQ.peekFirst()==nums[left]){
                    minQ.pollFirst();
                }
                left+=1;
            }
            ans=Math.max(ans, right-left+1);
        }
        return ans;
    }
}
