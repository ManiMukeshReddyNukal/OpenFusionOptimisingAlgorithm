"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
    
        def dfs( a, b, c, d):
            initial=grid[a][b]
            isLeaf=True
            for i in range(a,c+1):
                for j in range(b,d+1):
                    if grid[i][j]!=initial:
                        isLeaf=False
                        break
            if isLeaf:
                return Node(grid[a][b],True)
            topleft=dfs(a, b, (a+c)//2, (b+d)//2)
            bottomleft=dfs((a+c)//2+1, b,c , (b+d)//2)
            topright=dfs(a, (b+d)//2+1, (a+c)//2, d)
            bottomright=dfs((a+c)//2+1, (b+d)//2+1, c, d)
            return Node(grid[a][b],False,topleft,topright,bottomleft,bottomright)
        return dfs( 0, 0, len(grid)-1, len(grid[0])-1)
        
