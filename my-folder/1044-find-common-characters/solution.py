from typing import List
from collections import Counter

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        # Initialize the frequency dictionary with the counts of the first word
        freq = Counter(words[0])
        
        # Intersect the character counts with the rest of the words
        for word in words[1:]:
            freq &= Counter(word)  # This operation updates `freq` to the intersection

        # Create a list of characters repeated according to their minimum frequency
        result = []
        for char in freq:
            result.extend([char] * freq[char])  # Extend the list by the count of each char
        
        return result

