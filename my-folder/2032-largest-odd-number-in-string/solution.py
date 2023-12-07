class Solution(object):
    def largestOddNumber(self, num):
        """
        :type num: str
        :rtype: str
        """
        # Iterate from the end of the string
        for i in range(len(num) - 1, -1, -1):
            # Check if the digit is odd
            if int(num[i]) % 2 == 1:
                # Return the substring from the start to the odd digit (inclusive)
                return num[:i + 1]
        
        # Return an empty string if no odd digit is found
        return ""

