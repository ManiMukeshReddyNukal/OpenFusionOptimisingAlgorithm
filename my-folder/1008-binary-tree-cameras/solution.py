# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        self.output=0
        def dfs(node):
            if not node:
                return False,True
            lcamera,ltrack=dfs(node.left)
            rcamera,rtrack=dfs(node.right)
            camera,track=False,False
            if lcamera or rcamera:
                track=True
            if not ltrack or not rtrack:
                camera=True
                self.output+=1
                track=True
            return camera,track
        c,m=dfs(root)
        return self.output if m else self.output+1

