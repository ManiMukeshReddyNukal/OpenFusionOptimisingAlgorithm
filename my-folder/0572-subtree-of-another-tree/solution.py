# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """
        def isIdentical(root1,root2):
            if root1 is None or root2 is None:
                return root1 is None and root2 is None
            return ( root1.val==root2.val) and isIdentical(root1.left,root2.left) and isIdentical(root1.right,root2.right)  
        def dfs(node):
            if node is None:
                return False
            elif isIdentical(node,subRoot):
                return True
            return dfs(node.left) or dfs(node.right)
        return dfs(root)        
