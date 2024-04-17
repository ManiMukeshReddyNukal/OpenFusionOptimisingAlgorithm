# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        self.smalleststring=""
        self.dfs(root,"")
        return self.smalleststring
    def dfs(self,node,current_string):
        if not node:
            return
        current_string=chr(node.val+ord('a'))+current_string
        if not node.left and not node.right:
            if not self.smalleststring or self.smalleststring>current_string:
                self.smalleststring=current_string
        if node.left:
            self.dfs(node.left,current_string)
        if node.right:
            self.dfs(node.right,current_string)
