from typing import List

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        # Find the sum of the first `n - k` elements (the subarray we're not taking cards from)
        total_sum = sum(cardPoints)
        window_size = n - k
        min_window_sum = curr_window_sum = sum(cardPoints[:window_size])
        
        # Slide the window from left to right
        for i in range(1, k + 1):
            curr_window_sum = curr_window_sum - cardPoints[i - 1] + cardPoints[window_size + i - 1]
            min_window_sum = min(min_window_sum, curr_window_sum)
        
        # The maximum score is total_sum - min_window_sum
        return total_sum - min_window_sum

