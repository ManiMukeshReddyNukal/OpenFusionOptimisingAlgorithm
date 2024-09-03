class Solution:
    def reverseWords(self, s: str) -> str:
        s = self.trim(s)
        s = self.reverse(s, 0, len(s) - 1)
        s = self.reverse_each_word(s)
        return s

    def trim(self, s: str) -> str:
        left, right = 0, len(s) - 1
        while left < len(s) and s[left] == " ":
            left += 1
        while right >= 0 and s[right] == " ":
            right -= 1
        
        output = []
        while left <= right:
            if s[left] != " ":
                output.append(s[left])
            elif output and output[-1] != " ":
                output.append(s[left])
            left += 1
            
        return "".join(output)
    
    def reverse(self, s: str, left: int, right: int) -> str:
        s = list(s)  # Convert to list for mutable operations
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return "".join(s)  # Convert back to string
    
    def reverse_each_word(self, s: str) -> str:
        s = list(s)  # Convert to list for mutable operations
        n = len(s)
        left = 0
        while left < n:
            right = left
            while right < n and s[right] != " ":
                right += 1
            self.reverse_list(s, left, right - 1)
            left = right + 1
        return "".join(s)  # Convert back to string
    
    def reverse_list(self, s: list, left: int, right: int) -> None:
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

