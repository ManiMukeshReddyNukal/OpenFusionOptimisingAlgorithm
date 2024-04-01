# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        s=[root.val]
        def dfs(node):
            if not node:
                return 0
            leftsum=max(dfs(node.left),0)
            rightsum=max(dfs(node.right),0)
            s[0]=max(s[0],leftsum+rightsum+node.val)
            return max(max(leftsum,rightsum)+node.val,node.val)
        res=dfs(root)
        return s[0]
