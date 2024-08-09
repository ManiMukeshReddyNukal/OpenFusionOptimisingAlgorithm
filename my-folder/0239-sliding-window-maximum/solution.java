class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
     Deque<Integer> dq = new LinkedList<>();
     List<Integer> resp = new ArrayList();
     for(int i=0; i< nums.length; i++){
        while (!dq.isEmpty() && dq.peekFirst()<(i-k+1)){
            dq.pollFirst();
        }
        while (!dq.isEmpty() && nums[dq.peekLast()] < nums[i]){
            dq.pollLast();
        }
        dq.addLast(i);
        if(i>=k-1){
            resp.add(nums[dq.peekFirst()]);
        }
     }
     return resp.stream().mapToInt(Integer::intValue).toArray();   
    }
}
