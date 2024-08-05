class Solution {
    public int lengthOfLongestSubstring(String s) {
        int l=0;
        int r=0;
        int longest=0;
        Set<Character> set = new HashSet<>();
        while (r<s.length()){
            char ch = s.charAt(r);
            while (set.contains(ch)){
                set.remove(s.charAt(l));
                l++;
            }
            longest=Math.max(longest,r-l+1);
            set.add(s.charAt(r));
            r++;
        }
        return longest;
    }
}
