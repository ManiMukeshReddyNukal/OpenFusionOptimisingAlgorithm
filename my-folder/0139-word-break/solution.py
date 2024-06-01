class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[0] = True  # Base case: empty string can always be segmented

        def check(i):
            if dp[i]:
                return True
            for word in wordDict:
                if i >= len(word) and dp[i - len(word)] and s[i - len(word):i] == word:
                    dp[i] = True
                    return True
            return False

        for i in range(1, len(s) + 1):
            check(i)

        return dp[len(s)]

