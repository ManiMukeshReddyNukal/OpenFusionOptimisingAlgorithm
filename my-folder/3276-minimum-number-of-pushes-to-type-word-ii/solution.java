class Solution {
    public int minimumPushes(String word) {
        int[] freq=new int[26];
        Arrays.fill(freq, 0);
        for (char ch : word.toCharArray()){
            freq[ch-'a']+=1;
        }
        Arrays.sort(freq);
        int totalPushes=0;
        for (int i=25; i>=0 ; i--){
            if(freq[i]==0){break;}
            totalPushes+=( ( (25-i) / 8 ) +1 )*freq[i];
        }
        return totalPushes;

    }
}
