class Solution {
    public int maxDistance(List<List<Integer>> arrays) {
        int n= arrays.size();
        int n1=arrays.get(0).size();
        int minV = arrays.get(0).get(0);
        int maxV= arrays.get(0).get(arrays.get(0).size()-1);
        int res = 0;
        for ( int i=1; i< n; i++){
            int n2 = arrays.get(i).size(); 
            res=Math.max(res, Math.max(Math.abs(arrays.get(i).get(n2-1)-minV), Math.abs(maxV-arrays.get(i).get(0))));
            minV=Math.min(minV, arrays.get(i).get(0));
            maxV=Math.max(maxV, arrays.get(i).get(n2-1));
        }
        return res;

    }
}
