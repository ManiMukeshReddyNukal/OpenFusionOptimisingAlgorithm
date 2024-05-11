# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isbst(root):
            maxleft,minright = None, None
            minleft,maxright = None,None
            leftbst,rightbst = True,True
            if root.left:
                leftbst,minleft,maxleft = isbst(root.left)
            if root.right:
                rightbst,minright,maxright = isbst(root.right)
            if not(rightbst and leftbst): return (False, None, None)
            if minright != None and maxleft!=None:
                return (maxleft<root.val<minright, min(root.val,minleft,minright), max(root.val,maxleft,maxright))
            if minright!= None:
                return (root.val<minright, min(root.val,minright), max(root.val,maxright))
            if maxleft!= None:
                return (maxleft<root.val, min(root.val,minleft), max(root.val,maxleft))
            return (True,root.val,root.val)
        return isbst(root)[0]
