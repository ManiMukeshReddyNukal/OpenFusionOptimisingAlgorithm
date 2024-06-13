class Solution {
    public String mergeAlternately(String word1, String word2) {
        int m=word1.length();
        int n=word2.length();
        StringBuilder str= new StringBuilder();
        int i=0, j=0;
        while ( i<m || j <n){
            if (i<m){
                str.append(word1.charAt(i++));
            }
            if (j<n){
                str.append(word2.charAt(j++));
            }
        }
        return str.toString();
    }
}
