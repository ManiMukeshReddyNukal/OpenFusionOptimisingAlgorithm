class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq=Counter(tasks)
        maxf=max(freq.values())
        s=sum([maxf==f for k,f in freq.items()])
        return max(len(tasks), (n+1)*(maxf-1)+s)
