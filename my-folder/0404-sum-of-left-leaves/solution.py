# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        def isleaf(node):
            return node is not None and node.left is None and node.right is None
        stack=[root]
        total=0
        while stack:
            node=stack.pop()
            if isleaf(node.left):
                total+=node.left.val
            if node.right is not None:
                stack.append(node.right)
            if node.left is not None:
                stack.append(node.left)
        return total
