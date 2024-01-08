# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        ans = {'total': 0}
        def dfs(node):
            if node:
                if low<=node.val<=high:
                     ans['total']+=node.val
                if low<node.val:
                    dfs(node.left)
                if node.val<high:
                    dfs(node.right)
        dfs(root)
        return  ans['total']
        
