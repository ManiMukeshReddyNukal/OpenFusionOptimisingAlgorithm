class Solution {
    public int gcd(int length1, int length2){
        if (length2==0){
            return length1;
        }
        else{
            return gcd(length2, length1 % length2);
        }
    }
    public String gcdOfStrings(String str1, String str2) {
        if (!(str1+str2).equals(str2+str1))
        {
            return "";
        }
        int gcdlength=gcd(str1.length(), str2.length());
        return str1.substring(0,gcdlength);
    }
}
