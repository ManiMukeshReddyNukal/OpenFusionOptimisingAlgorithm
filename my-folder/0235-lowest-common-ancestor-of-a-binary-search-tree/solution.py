# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def pathfromroot(node, root):
            if root==None:
                return deque()
            if node.val==root.val:
                return deque([node])
            leftp = pathfromroot(node, root.left)
            rightp = pathfromroot(node, root.right)
            if len(leftp)==0 and len(rightp)==0:
                return leftp
            if len(leftp)==0:
                rightp.appendleft(root)
                return rightp
            leftp.appendleft(root)
            return leftp
        leftpath = list(pathfromroot(p,root))
        rightpath = list(pathfromroot(q,root))
        # print(leftpath)
        # print(rightpath)
        ind = 0
        for i in range(max(len(leftpath), len(rightpath))):
            if i>=len(leftpath) or i>=len(rightpath) or leftpath[i]!=rightpath[i]:
                break
            ind=i
        return leftpath[ind]
        # return None
            

