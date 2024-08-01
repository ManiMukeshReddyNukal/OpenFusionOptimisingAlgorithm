class Solution:
    def trim(self, s):
        left, right = 0, len(s) - 1
        while left <= right and s[left] == " ":
            left += 1
        while left <= right and s[right] == " ":
            right -= 1
        output = []
        while left <= right:
            if s[left] != " ":
                output.append(s[left])
            elif output[-1] != " ":
                output.append(s[left])
            left += 1
        return output

    def reverse(self, l, left, right):
        while left < right:
            l[left], l[right] = l[right], l[left]
            left += 1
            right -= 1

    def reverse_each_word(self, l):
        left, right = 0, 0
        while left < len(l):
            while right < len(l) and l[right] != " ":
                right += 1
            # Reverse the current word
            self.reverse(l, left, right - 1)
            left = right + 1
            right += 1

    def reverseWords(self, s: str) -> str:
        l = self.trim(s)  # Remove leading/trailing and multiple spaces
        print(l)
        self.reverse(l, 0, len(l) - 1)  # Reverse the entire list
        self.reverse_each_word(l)  # Reverse each word
        print(l)
        return "".join(l)  # Join the list into a string

