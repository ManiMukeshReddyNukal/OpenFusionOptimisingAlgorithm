# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(root,currentsum):
            if not root:return False
            currentsum=currentsum+root.val
            if not root.left and not root.right:
                return currentsum==targetSum
            return dfs(root.left,currentsum) or dfs(root.right, currentsum)
        return dfs(root, 0)
