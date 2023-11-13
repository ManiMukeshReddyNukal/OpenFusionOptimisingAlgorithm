# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = [root.val]
        def dfs(node):
            if not node:
                return 0
            leftMax=max(dfs(node.left),0)
            rightMax=max(dfs(node.right),0)
            res[0]=max(res[0],node.val+leftMax+rightMax)
            return node.val+max(leftMax,rightMax)
        
        dfs(root)
        return res[0]
        
