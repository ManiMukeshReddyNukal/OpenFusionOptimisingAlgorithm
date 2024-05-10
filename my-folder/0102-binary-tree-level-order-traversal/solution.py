from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        q = [root]
        lot = []
        while q:
            lot.append([x.val for x in q])
            q1 = []
            for node in q:
                if node.left: q1.append(node.left)
                if node.right: q1.append(node.right)
            q=q1
        return lot
            
