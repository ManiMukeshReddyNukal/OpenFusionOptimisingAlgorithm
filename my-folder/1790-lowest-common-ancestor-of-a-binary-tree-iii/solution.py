"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        def pathtopar(p):
            path = []
            parent = p.parent
            path.append(p)
            while parent:
                path.append(parent)
                parent=parent.parent
            return path
        left = list(reversed(pathtopar(p)))
        right = list(reversed(pathtopar(q)))
        ind = 0
        for i in range(min(len(left),len(right))):
            if left[i] == right[i]:
                ind = i
            else: break
        return left[ind]
