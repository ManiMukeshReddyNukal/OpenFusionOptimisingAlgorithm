# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        q=deque()
        q.append(root)
        if not root:
            return []
        result=[]
        while q:
            r=[]
            n=len(q)
            for _ in range(n):
                node=q.popleft()
                if node:
                    if node.left: q.append(node.left)
                    if node.right: q.append(node.right)
                    r.append(node.val)
            result.append(r)
        return result[::-1]

