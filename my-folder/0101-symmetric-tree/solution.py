# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isMirror(self,left,right):
        if left is None and right is None:
            return True
        if left is None and right is not None:
            return False
        if left is not None and right is None:
            return False
        if left.val==right.val and self.isMirror(left.left,right.right) and self.isMirror(left.right,right.left):
            return True
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.isMirror(root.left, root.right)
