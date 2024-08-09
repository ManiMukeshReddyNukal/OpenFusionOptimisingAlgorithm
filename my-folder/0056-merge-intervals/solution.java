class Solution {
    public int[][] merge(int[][] intervals) {
        Comparator<int[]> compare = (a,b)-> a[0]-b[0];
        Arrays.sort(intervals , compare);
        List<int[]> merged = new ArrayList<>();
        merged.add(intervals[0]);
        for(int i=1; i<intervals.length; i++){
            if(merged.get(merged.size()-1)[1]<intervals[i][0]){
                merged.add(intervals[i]);
            }
            else{
                merged.set(merged.size()-1, new int[] { merged.get(merged.size()-1)[0], Math.max(merged.get(merged.size()-1)[1],intervals[i][1])});
            }
        }
        return merged.stream().toArray(int[][]::new);
    }
}
