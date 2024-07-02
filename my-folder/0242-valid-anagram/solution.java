class Solution {
    public boolean isAnagram(String s, String t) {
        int n=s.length();
        int m=t.length();
        if (n!=m){
            return false;
        }
        int[] counter = new int[26];
        for ( int i=0; i<n; i++){
            counter[s.charAt(i)-'a']++;
            counter[t.charAt(i)-'a']--;
            }
        for ( int count: counter){
            if (count!=0){
                return false;
            }
        }
        return true;
        }
}
