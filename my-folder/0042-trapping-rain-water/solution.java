class Solution {
    public int trap(int[] height) {
        int n=height.length;
        int[] leftmax=new int[n];
        int[] rightmax=new int[n];
        int left=0;
        leftmax[0]=left;
        for (int i=1; i<n ; i++){
            left=Math.max(height[i-1],left);
            leftmax[i]=left;
        }
        int right=0;
        rightmax[n-1]=right;
        for (int i=n-2; i>-1 ; i--){
            right=Math.max(height[i+1],right);
            rightmax[i]=right;
        }

        int water=0;
        for (int i=1; i<n-1 ; i++){
            if (Math.min(leftmax[i],rightmax[i]) > height[i])
            water+=Math.min(leftmax[i],rightmax[i]) - height[i];
        }
        return water;

    }
}
