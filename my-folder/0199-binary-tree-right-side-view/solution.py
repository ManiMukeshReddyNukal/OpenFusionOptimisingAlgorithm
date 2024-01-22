# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q=[]
        q.append(root)
        r=[]
        if root is None:
            return None
        while q!=[]:
            r.append(q[-1].val)
            nq=[]
            for i in range(len(q)):
                node=q[i]
                if node.left:
                    nq.append(node.left)
                if node.right:
                    nq.append(node.right)
            q=nq
        return r


