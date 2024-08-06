class Solution {
    public int[][] kClosest(int[][] points, int k) {
        PriorityQueue<int[]> pq= new PriorityQueue<>((a,b) -> b[0]-a[0]);
        for (int i=0; i< points.length; i++){
            int[] entry = {squareddistance(points[i]),i};
            pq.add(entry);
            if (pq.size()>k) {
                pq.poll();
            }
        }
        int[][] resp = new int[k][2];
        int i=0;
        while (!pq.isEmpty()){
            resp[i]=points[pq.poll()[1]];
            i++;
        }
        return resp;
    }

    public int squareddistance(int[] point){
        return point[0]*point[0]+point[1]*point[1];
    }
}
