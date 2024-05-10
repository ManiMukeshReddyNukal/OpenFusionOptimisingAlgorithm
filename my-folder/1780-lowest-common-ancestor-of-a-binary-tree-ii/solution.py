# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def lca(root, p, q):
            if root==None: return (None, False)
            if root.val==p.val: 
                left = lca(p, TreeNode(None),q)
                if left[0]==None: return (p, False)
                else: return (p, True)
            if root.val==q.val: 
                right = lca(q,p,TreeNode(None))
                if right[0]==None: return (q, False)
                else: return (q, True)
            left = lca(root.left,p,q)
            right = lca(root.right,p,q)
            if not left[0] and not right[0]:
                return (None, False)
            if not left[0]:
                return right
            if not right[0]:
                return left
            return (root, True)
        val = lca(root,p,q)
        return val[0] if val[1] else None
