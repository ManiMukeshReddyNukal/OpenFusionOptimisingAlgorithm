class Solution {
    public int numTeams(int[] rating) {
        int result=0;
        for (int i = 0; i < rating.length; i++) {
            int left_small=0;
            int right_larger=0;
            int left_larger=0;
            int right_smaller=0;
            for (int j = 0; j < i; j++) {
                if(rating[j]<rating[i]){
                    left_small++;
                }
            }
            for (int j2 = i+1; j2 < rating.length; j2++) {
                if (rating[j2]>rating[i]){
                    right_larger++;
                }
            }
            result+=left_small*right_larger;
            left_larger=i-left_small;
            right_smaller=rating.length-1-i-right_larger;
            result+=left_larger*right_smaller;
        }
        return result;
    }
}
