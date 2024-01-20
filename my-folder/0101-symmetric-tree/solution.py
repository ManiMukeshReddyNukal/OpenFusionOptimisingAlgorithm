# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        return self.isMirror(root.left,root.right)
    def isMirror(self,l,r):
        if l is None and r is None:
            return True
        if l is None or r is None:
            return False
        return (l.val==r.val) and self.isMirror(l.right,r.left) and self.isMirror(l.left,r.right)
