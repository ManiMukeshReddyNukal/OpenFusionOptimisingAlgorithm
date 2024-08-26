class Solution {
    public int lengthOfLIS(int[] nums) {
        List<Integer> list = new ArrayList<>();
        list.add(nums[0]);
        for(int i=1; i<nums.length; i++){
            int num = nums[i];
            if (list.get(list.size()-1)<num)list.add(num);
            else{
                int idx= binarySearch(list,num);
                list.set(idx,num);
            }
        }
        return list.size();   
    }

    public int binarySearch(List<Integer> list , int num){
        int left=0;
        int right=list.size()-1;
        int mid=(left+right)/2;
        while (left<right){
            mid=(left+right)/2;
            if(list.get(mid)==num){
                return mid;
            }
            else if(list.get(mid)>num){
                right=mid;
            } 
            else{
                left=mid+1;
            }
        }
        return left;
    }
}
