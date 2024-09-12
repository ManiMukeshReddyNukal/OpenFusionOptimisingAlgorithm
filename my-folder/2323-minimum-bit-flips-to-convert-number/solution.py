class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        react= start^goal
        count=0
        while(react):
            count+=react&1
            react>>=1
        return count
