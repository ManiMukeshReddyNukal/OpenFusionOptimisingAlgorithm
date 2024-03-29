class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        prob=[float('-inf')]*n
        prob[start_node]=1
        for i in range(n-1):
            temp=prob[:]
            updated = False
            for [s,d],w in zip(edges,succProb):
                if temp[s]!=float('-inf') and temp[d]<prob[s]*w:
                    temp[d]=prob[s]*w
                    updated = True
                if temp[d]!=float('-inf') and temp[s]<prob[d]*w:
                    temp[s]=prob[d]*w
                    updated = True  
            prob=temp
            if not updated:
                break
        return prob[end_node] if prob[end_node] > 0 else 0
