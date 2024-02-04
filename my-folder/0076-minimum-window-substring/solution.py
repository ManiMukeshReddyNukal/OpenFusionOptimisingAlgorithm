class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or len(t) > len(s):
            return ""
        
        # Dictionary to count characters in t
        countT = {}
        for c in t:
            countT[c] = countT.get(c, 0) + 1
        
        # Initialize window pointers and the count for characters in the current window
        l, r = 0, 0
        count = {}
        minLength = float('inf')
        resp = ""
        
        # Variable to keep track of how many characters from t are currently matched in the window
        have, need = 0, len(countT)
        
        while r < len(s):
            # Add the current character to the window
            count[s[r]] = count.get(s[r], 0) + 1
            if s[r] in countT and count[s[r]] == countT[s[r]]:
                have += 1
            
            # Shrink the window from the left if it already contains all needed characters
            while have == need:
                # Update the response if the current window is smaller
                if (r - l + 1) < minLength:
                    minLength = r - l + 1
                    resp = s[l:r+1]
                
                # Remove the leftmost character from the window
                count[s[l]] -= 1
                if s[l] in countT and count[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
            
            # Expand the window by moving right
            r += 1
        
        return resp

