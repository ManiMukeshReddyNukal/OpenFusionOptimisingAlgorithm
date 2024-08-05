class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        if (strs.length==0) return new ArrayList<>();
        Map<String,List> mp = new HashMap<>();
        int[] count= new int[26];
        for (String st: strs){
            Arrays.fill(count, 0);
            for ( char c : st.toCharArray()) count[c-'a']++;
            StringBuilder sb = new StringBuilder("");
            for (int i = 0; i < count.length; i++) {
                sb.append("#");
                sb.append(count[i]);
            }
            String key= sb.toString();
            if(!mp.containsKey(key)){mp.put(key, new ArrayList<>());}
            mp.get(key).add(st);

        }
        return new ArrayList(mp.values());
    }
}
