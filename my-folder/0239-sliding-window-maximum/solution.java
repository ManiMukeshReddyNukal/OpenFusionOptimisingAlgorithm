class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        Deque<Integer> deque = new LinkedList<>();
        List<Integer> resp= new ArrayList<>();
        for (int i = 0; i < nums.length; i++) {
            while (!deque.isEmpty() && deque.peekFirst()<(i-k+1)){
                deque.pollFirst();
            }
            while (!deque.isEmpty() && nums[deque.peekLast()]<nums[i]){
                deque.pollLast();
            }
            deque.addLast(i);
            if (i>=k-1){
                resp.add(nums[deque.peekFirst()]);
            }
        }
        return resp.stream().mapToInt(Integer::intValue).toArray();
    }
}
