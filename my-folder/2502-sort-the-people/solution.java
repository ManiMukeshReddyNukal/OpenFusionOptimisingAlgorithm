class Solution {
    public String[] sortPeople(String[] names, int[] heights) {
        int n=names.length;
        Map<Integer,String> heightToName= new HashMap<>();
        for ( int i=0; i<n; i++){
            heightToName.put(heights[i], names[i]);
        }
        Arrays.sort(heights);
        String[] response = new String[n];
        for ( int i=0; i<n ; i++){
            response[n-i-1]=heightToName.get(heights[i]);
        }
        return response;
    }
}
