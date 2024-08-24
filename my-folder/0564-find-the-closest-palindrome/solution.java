class Solution {
    public String nearestPalindromic(String n) {
        int len = n.length();
        int midIndex=len%2==0?len/2-1:len/2;
        long firtHalf = Long.parseLong(n.substring(0, midIndex+1));
        List<Long> possibilities = new ArrayList<>();
        possibilities.add(generatePalindrome(firtHalf,len%2==0));
        possibilities.add(generatePalindrome(firtHalf+1,len%2==0));
        possibilities.add(generatePalindrome(firtHalf-1,len%2==0));
        possibilities.add((long)Math.pow(10, len-1)-1);
        possibilities.add((long)Math.pow(10, len)+1);

        long diff = Long.MAX_VALUE;
        long res=0;
        long base= Long.parseLong(n);
        for (long cand : possibilities){
            if (cand==base) continue;
            if (Math.abs(cand-base) < diff){
                diff=Math.abs(cand-base);
                res=cand;
            }
            else if(Math.abs(cand-base)==diff){
                res=Math.min(res, cand);
            }
        }
        return String.valueOf(res);
        
    }

    public long generatePalindrome(long left, boolean even){
        long resp = left;
        if (!even)left=left/10;
        while(left>0){
            resp=resp*10+(left%10);
            left=left/10;
        }
        return resp;
    }
}
