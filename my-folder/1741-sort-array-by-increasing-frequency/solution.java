class Solution {
    public int[] frequencySort(int[] nums) {
        Map<Integer,Integer> mp= new HashMap<>();
        Integer[] out = new Integer[nums.length];
        for (int num:nums){
            mp.put(num, mp.getOrDefault(num, 0)+1);
        }
        for (int i=0; i<nums.length;i++){
            out[i]=nums[i];
        }
        Arrays.sort(out,(a,b)->{
            if(mp.get(a).equals(mp.get(b))){
                return Integer.compare(b, a);
            }else{
                return Integer.compare(mp.get(a),mp.get(b));
            }
        });
        for (int i=0; i<nums.length;i++){
            nums[i]=out[i];
        }

        return nums;
    }
}
