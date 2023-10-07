class Solution(object):
    def numOfArrays(self, n, m, k):
        MOD = 10**9 + 7
        T = [[[-1 for _ in range(101)] for _ in range(51)] for _ in range(51)]
        
        def solve(idx, searchCost, maxSoFar):
            if idx == n:
                if searchCost == k:
                    return 1
                return 0
            if T[idx][searchCost][maxSoFar] != -1:
                return T[idx][searchCost][maxSoFar]
            result = 0
            for i in range(1, m + 1):  # Iterate from 1 to m
                if i > maxSoFar:
                    result = (result + solve(idx + 1, searchCost + 1, i)) % MOD
                else:
                    result = (result + solve(idx + 1, searchCost, maxSoFar)) % MOD
            T[idx][searchCost][maxSoFar] = result % MOD
            return T[idx][searchCost][maxSoFar]
        
        return solve(0, 0, 0)

