# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        maxD=-1
        leftnode=None
        def dfs(node,depth):
            if not node:
                return None
            nonlocal maxD
            nonlocal leftnode
            if depth>maxD:
                leftnode=node.val
                maxD=depth
            dfs(node.left,depth+1)
            dfs(node.right,depth+1)
        dfs(root,0)
        return leftnode
