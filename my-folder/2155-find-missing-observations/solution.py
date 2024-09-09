class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        total_sum = (len(rolls) + n) * mean - sum(rolls)
        if total_sum < n or total_sum > 6 * n:
            return []
        result = [total_sum // n for _ in range(n)]
        remainder = total_sum % n
        for i in range(remainder):
            result[i] += 1
        return result
