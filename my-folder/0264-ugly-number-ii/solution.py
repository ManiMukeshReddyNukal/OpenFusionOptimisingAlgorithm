class Solution:
    def nthUglyNumber(self, n: int) -> int:
        minheap = []
        visited = set()
        primes = [2, 3, 5]
        heapq.heappush(minheap, 1)
        val = 1
        visited.add(val)
        for _ in range(n):
            val = heapq.heappop(minheap)
            for prime in primes:
                new_val = prime * val
                if new_val not in visited:
                    heapq.heappush(minheap, new_val)
                    visited.add(new_val)
        return val
