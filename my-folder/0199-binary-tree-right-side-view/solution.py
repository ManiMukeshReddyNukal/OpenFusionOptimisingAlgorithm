# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        rpath = self.rightSideView(root.right)
        lpath = self.rightSideView(root.left)
        rpath.insert(0,root.val)
        lpath.insert(0,root.val)
        if len(lpath)<=len(rpath):
            return rpath
        return rpath+lpath[len(rpath):]


