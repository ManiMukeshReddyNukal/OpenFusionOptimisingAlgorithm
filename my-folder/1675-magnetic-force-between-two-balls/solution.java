class Solution {
    public boolean canPlaceBalls(int[] position, int distance, int m)
    {
        int prev_position=position[0];
        int balls_placed=1;
        for ( int p : position)
        {
            if ( (p-prev_position) >= distance)
            {
                prev_position=p;
                balls_placed++;
            }
            if (balls_placed==m){
                return true;
            }
        }
        return false;
    }
    public int maxDistance(int[] position, int m) {
        int res=0;
        Arrays.sort(position);
        int min=1;
        int max=(int)(position[position.length-1]/(m-1.0))+1;
        int mid=-1;
        while ( min<=max){
            mid=(min+max)/2;
            if (canPlaceBalls(position, mid, m)) 
            {
                res=mid;
                min=mid+1;
            }
            else{
                max=mid-1;
            }
        }
        return res;
    }
}
