# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def count(root, num, maxval):
            if not root: return
            if root.val>=maxval:
                num[0]+=1
            count(root.left,num,max(root.val,maxval))
            count(root.right,num,max(root.val,maxval))
        num = [0]
        count(root,num,root.val)
        return num[0]
