class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        n = len(s)
        m = len(t)
        i = 0
        j = 0
        
        # Iterate through both strings
        while i < n and j < m:
            if s[i] == t[j]:
                j += 1  # Move to the next character in t if there's a match
            i += 1  # Always move to the next character in s

        # If we have matched all characters of t in s, j will be equal to m
        return m - j
