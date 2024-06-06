# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxpath=-math.inf
        def recursive(node):
            nonlocal maxpath
            if not node:
                return 0
            leftvalue=max(recursive(node.left),0)
            rightvalue=max(recursive(node.right),0)
            maxpath=max(maxpath, leftvalue+rightvalue+node.val)
            return max(leftvalue+node.val,rightvalue+node.val)
        recursive(root)
        return maxpath


