class Solution {
    public String longestPalindrome(String s) {
        String resp = "";
        int n = s.length();
        if (n == 1) {
            return s;
        }
        resp = s.substring(0, 1);  // Initialize with the first character
        boolean[][] dp = new boolean[n][n];
        
        for (int i = 0; i < n; i++) {
            dp[i][i] = true;
        }
        
        for (int i = 0; i < n - 1; i++) {
            if (s.charAt(i) == s.charAt(i + 1)) {
                dp[i][i + 1] = true;
                resp = s.substring(i, i + 2);
            }
        }

        for (int diff = 2; diff < n; diff++) {
            for (int i = 0; i < n - diff; i++) {
                int j = i + diff;
                if (s.charAt(i) == s.charAt(j) && dp[i + 1][j - 1]) {
                    dp[i][j] = true;
                    resp = s.substring(i, j + 1);
                }
            }
        }
        
        return resp;
    }
}

