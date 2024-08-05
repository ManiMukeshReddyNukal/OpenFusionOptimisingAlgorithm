class Solution {
    public String minWindow(String s, String t) {
        int[] resp={-1,0,0};
        int[] tfreq=new int[128];
        Arrays.fill(tfreq,0);
        int needed=0;
        for(char ch : t.toCharArray()){
            if(tfreq[ch]==0)
            {
                needed++;
            }
            tfreq[ch]+=1;
        }
        int[] sfreq=new int[128];
        Arrays.fill(sfreq,0);
        int l=0;
        int r=0;
        int matching=0;
        int minlength=Integer.MAX_VALUE;
        while (r<s.length()){
            sfreq[s.charAt(r)]+=1;
            if (sfreq[s.charAt(r)]==tfreq[s.charAt(r)]){
                matching+=1;
            }
            while (matching==needed){
                if ((r-l+1)<minlength){
                    minlength=r-l+1;
                    resp[0]=0;
                    resp[1]=l;
                    resp[2]=r;
                }
                sfreq[s.charAt(l)]-=1;
                if ( tfreq[s.charAt(l)] >0 && tfreq[s.charAt(l)] >sfreq[s.charAt(l)] ){
                    matching--;
                }
                l++;
            }
            r++;
        }
        return resp[0] > -1? s.substring(resp[1], resp[2]+1):"";
    }
}
