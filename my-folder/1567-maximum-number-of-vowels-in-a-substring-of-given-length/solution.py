class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        n = len(s)
        temps = s[:k]
        count = temps.count('a')+temps.count('e')+temps.count('i')+temps.count('o')+temps.count('u')
        maxcount = count
        for i in range(1,n-k+1):
            count -= 1 if s[i-1] in 'aeiou' else 0
            count += 1 if s[i+k-1] in 'aeiou' else 0
            # print(count)
            maxcount = max(maxcount, count)
        return  maxcount

