# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def preorder(node,currSum):
            nonlocal count
            if not node:
                return
            currSum+=node.val
            if currSum==targetSum:
                count+=1
            count+=h[currSum-targetSum]
            h[currSum]+=1
            preorder(node.left, currSum)
            preorder(node.right, currSum)
            h[currSum]-=1
        count=0
        h=defaultdict(int)
        preorder(root, 0)
        return count
