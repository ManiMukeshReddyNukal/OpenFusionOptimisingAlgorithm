class Solution {
    public int characterReplacement(String s, int k) {
        List<Integer> freq = new ArrayList<>(Collections.nCopies(26, 0));
        int l=0;
        int resp=0;
        for (int r=0; r<s.length(); r++){
            freq.set(s.charAt(r)-'A',1+freq.get(s.charAt(r)-'A'));
            while  (r-l+1 - Collections.max(freq) >k ){
                freq.set(s.charAt(l)-'A',freq.get(s.charAt(l)-'A')-1);
                l++;
            }
            resp=Math.max(resp, r-l+1);
        }   
        return resp;

    }
}
