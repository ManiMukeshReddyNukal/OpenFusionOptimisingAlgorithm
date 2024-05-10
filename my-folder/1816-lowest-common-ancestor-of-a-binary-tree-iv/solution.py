# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        nodevals = {node.val for node in nodes}
        def lca(root, nodevals):
            if root==None: return None
            if root.val in nodevals: return root
            left = lca(root.left,nodevals)
            right = lca(root.right,nodevals)
            if left and right: return root
            return left or right
        return lca(root,nodevals)
