from typing import List

class Solution:
    def checkContradictions(self, equations: List[List[str]], values: List[float]) -> bool:
        dict = {}
        
        def find(x):
            if x not in dict:
                dict[x] = (x, 1)
            root, weight = dict[x]
            if root != x:
                new_root, new_weight = find(root)
                dict[x] = (new_root, new_weight * weight)
            return dict[x]
        
        def union(x, y, value):
            base_x, weight_x = find(x)
            base_y, weight_y = find(y)
            if base_x == base_y:
                if abs((weight_x / weight_y) - value) > 0.00001:
                    return True
                return False
            else:
                dict[base_x] = (base_y, value * weight_y / weight_x)
                return False
        
        for (a, b), v in zip(equations, values):
            if union(a, b, v):
                return True
        return False

