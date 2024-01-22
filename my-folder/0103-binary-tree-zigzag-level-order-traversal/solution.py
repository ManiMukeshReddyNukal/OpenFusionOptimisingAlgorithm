# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels=[]
        if not root:
            return levels
        q=[]
        dir=False
        q.append(root)
        while q!=[]:
            dq=[]
            for c in q:
                if c is not None:
                    if c.left:
                        dq.append(c.left)
                    if c.right:
                        dq.append(c.right)
            lr=[]
            while q!=[]:
                if dir:
                    lr.append(q.pop().val)
                else:
                    lr.append(q.pop(0).val)
            levels.append(lr)
            dir=not dir
            q=dq
        return levels
