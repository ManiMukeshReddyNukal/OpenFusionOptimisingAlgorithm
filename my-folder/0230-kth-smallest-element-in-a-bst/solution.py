# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        def popksmall(root,k,ksmall):
            if root==None: return 0
            num = 0
            if k>0:
                num += popksmall(root.left,k,ksmall)
            if num < k:
                ksmall.append(root.val)
                num += 1
            if num < k:
                num += popksmall(root.right, k-num, ksmall)
            return num
        ksmall = []
        popksmall(root,k,ksmall)
        return ksmall[-1]
