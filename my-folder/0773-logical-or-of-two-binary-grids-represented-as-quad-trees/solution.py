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
    def intersect(self, quadTree1: 'Node', quadTree2: 'Node') -> 'Node':
        def dfs(quadTree1,quadTree2):
            if quadTree1.isLeaf and quadTree2.isLeaf:
                return Node(quadTree1.val or quadTree2.val,True)
            if quadTree1.isLeaf:
                return quadTree1 if quadTree1.val else quadTree2
            if quadTree2.isLeaf:
                return quadTree2 if quadTree2.val else quadTree1
            node=Node()
            node.topLeft=dfs(quadTree1.topLeft, quadTree2.topLeft)
            node.topRight=dfs(quadTree1.topRight, quadTree2.topRight)
            node.bottomLeft=dfs(quadTree1.bottomLeft, quadTree2.bottomLeft)
            node.bottomRight=dfs(quadTree1.bottomRight, quadTree2.bottomRight)
            isLeaf=(node.topLeft.isLeaf and node.topRight.isLeaf and node.bottomLeft.isLeaf and node.bottomRight.isLeaf)
            sameval=(node.topLeft.val==node.topRight.val==node.bottomLeft.val==node.bottomRight.val)
            if isLeaf and sameval:
                return node.topLeft
            return node
        return dfs(quadTree1, quadTree2)
