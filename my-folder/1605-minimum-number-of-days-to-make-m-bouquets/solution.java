class Solution {
     private int getNoofBouqets( int[] bloomDay, int mid, int k){
        int nooofbouqets=0;
        int count=0;
            for ( int i=0; i<bloomDay.length; i++){
                if(bloomDay[i]<=mid){
                    count++;
                }
                else{
                    count=0;
                }
                if(count==k){
                    nooofbouqets++;
                    count=0;
                }
            }
            return nooofbouqets;
        }
    public int minDays(int[] bloomDay, int m, int k) {
       int start=0;
       int end=0;
       for (int day: bloomDay){
        end=Math.max(end,day);
       }
       int mindDays=-1;
       while (start <= end){
        int mid=(start+end)/2;
        if ( getNoofBouqets(bloomDay,mid,k)>=m){
            mindDays=mid;
            end=mid-1;
        }
        else{
            start=mid+1;
        }
       }
       return mindDays;
    }
}
