from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        # Special case when a new row needs to be added at the root
        if depth == 1:
            return TreeNode(val, left=root)

        # Helper function to add row at given depth
        def addOneRowTree(node: Optional[TreeNode], current_depth: int):
            if not node:
                return None
            if current_depth == depth - 1:
                # Add new nodes as left and right children of current node
                node.left = TreeNode(val, left=node.left)
                node.right = TreeNode(val, right=node.right)
            else:
                # Continue to traverse to reach the correct depth
                node.left = addOneRowTree(node.left, current_depth + 1)
                node.right = addOneRowTree(node.right, current_depth + 1)
            return node

        return addOneRowTree(root, 1)  # Start the recursion with the root at current_depth 1


