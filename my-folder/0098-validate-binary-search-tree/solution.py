class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node,left=-math.inf,right=math.inf):
            if not node:
                return True
            if node.val<=left or node.val>=right:
                return False
            return validate(node.left, left,node.val) and validate(node.right,node.val,right)
        return validate(root)
