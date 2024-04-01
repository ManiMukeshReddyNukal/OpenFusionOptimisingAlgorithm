# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q=[root]
        out=[]
        while q:
            n=len(q)
            nq=[]
            o=[]
            for i in range(n):
                node=q.pop(0)
                if node.left:
                    nq.append(node.left)
                if node.right:
                    nq.append(node.right)
                o.append(node.val)
            out.append(o)
            q=nq
        return out
