class SparseVector {
    
    public SortedSet<Integer> sortedSet;
    public int[] nums;

    SparseVector(int[] nums) {
        sortedSet=new TreeSet<>();
        this.nums=nums;
        for(int i=0; i<nums.length; i++){
            sortedSet.add(i);
        }
    }
    
	// Return the dotProduct of two sparse vectors
    public int dotProduct(SparseVector vec) {
        int ans=0;
        this.sortedSet.retainAll(vec.sortedSet);
        for (Integer in : this.sortedSet){
            ans+=this.nums[in]*vec.nums[in];
        }
        return ans;
    }
}

// Your SparseVector object will be instantiated and called as such:
// SparseVector v1 = new SparseVector(nums1);
// SparseVector v2 = new SparseVector(nums2);
// int ans = v1.dotProduct(v2);
