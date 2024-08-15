class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        Set<List<Integer>> resp = new HashSet();
        for (int i = 0; i < nums.length; i++) {
            if (i > 0 && nums[i] == nums[i - 1]) continue;
            if (nums[i]>0) {
                break;
            }
            int[] temparray = Arrays.copyOfRange(nums, i+1, nums.length);
            List<List<Integer>> out = twoSum(temparray, -1*nums[i]);
            if(out.size() !=0){
                for (int j = 0; j < out.size(); j++) {
                    resp.add(new ArrayList(Arrays.asList(nums[i],nums[i+1+out.get(j).get(0)],nums[i+1+out.get(j).get(1)])));
                }
            }
        }
        return new ArrayList(resp);
    }

    public List<List<Integer>> twoSum(int[] nums, int target) {
        Set<List<Integer>> resp = new HashSet<>();
        Map<Integer,Integer> mp=new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            if (mp.containsKey(target-nums[i])){
                resp.add(Arrays.asList(mp.get(target-nums[i]),i));
            }
            mp.put(nums[i], i);
        }
        return new ArrayList(resp);
    }
}
