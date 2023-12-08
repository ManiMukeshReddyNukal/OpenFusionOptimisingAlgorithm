# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def tree2str(self, root):
        """
        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return ""  # Return an empty string when the node is None
        result = str(root.val)  # Convert root.val to a string
        left_str = self.tree2str(root.left)
        right_str = self.tree2str(root.right)
        
        if left_str or right_str:
            result += "(" + left_str + ")"
        
        if right_str:
            result += "(" + right_str + ")"
        
        return result

