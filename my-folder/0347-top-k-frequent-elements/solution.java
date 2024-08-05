class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer,Integer> mp = new HashMap<>();
        for (int i : nums) {
            mp.put(i, mp.getOrDefault(i, 0)+1);
        }
        PriorityQueue<Integer> pq = new PriorityQueue<>((a,b)-> { return mp.getOrDefault(a,0)-mp.getOrDefault(b,0);});
        for (Integer integer : mp.keySet()) {
            pq.add(integer);
            if (pq.size()>k)pq.poll();           
        }
        int[] resp = new int[k];
        for (int i = 0; i < resp.length; i++) {
            resp[i]=pq.poll();
        }
        return resp;

    }
}
