class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] arr1=new int[nums.length];
        int[] arr2=new int[nums.length];
        int evenprod=1;
        int oddprod=1;
        arr1[0]=1;
        arr2[nums.length-1]=1;
        for (int i = 1; i < arr2.length; i++) {
            evenprod*=nums[i-1];
            arr1[i]=evenprod;
        }
        for (int i = arr2.length-2; i >-1; i--) {
            oddprod*=nums[i+1];
            arr2[i]=oddprod;
        }
        int[] out = new int[nums.length];
        for (int i = 0; i < arr2.length; i++) {
            out[i]=arr1[i]*arr2[i];
        }
        return out;
    }
}
