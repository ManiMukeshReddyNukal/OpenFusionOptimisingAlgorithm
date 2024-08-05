class Solution {
    public boolean isAnagram(String s, String t) {
        String[] sa=s.split("");
        String[] ta=t.split("");
        int n=sa.length;
        if(ta.length!=n){
            return false;
        }
        Arrays.sort(sa);
        Arrays.sort(ta);
        if (Arrays.equals(sa, ta)){
            return true;
        }
        else{
            return false;
        }
    }
}
