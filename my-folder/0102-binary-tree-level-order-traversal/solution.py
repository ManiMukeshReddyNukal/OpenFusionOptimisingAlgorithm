# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        level=[]
        if not root:
            return root
        level.append(root)
        out=[]
        while level:
            outi=[]
            level_temp=[]
            for _ in range(len(level)):
                node=level.pop(0)
                outi.append(node.val)
                if node.left: level_temp.append(node.left)
                if node.right: level_temp.append(node.right)
            out.append(outi)
            level=level_temp

        # Replace this placeholder return statement with your code
        return out
