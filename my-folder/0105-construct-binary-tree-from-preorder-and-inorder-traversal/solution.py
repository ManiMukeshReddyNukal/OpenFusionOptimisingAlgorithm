# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        indinpre = {}
        indinin = {}
        for i,x in enumerate(preorder):
            indinpre[x] = i
        for i,x in enumerate(inorder):
            indinin[x] = i
        def buildtree(ip, jp, ii,ji):
            if ip>jp: return None
            return TreeNode(preorder[ip], 
                buildtree(ip+1,ip+(indinin[preorder[ip]]-ii), ii, indinin[preorder[ip]]-1),
                buildtree(ip+(indinin[preorder[ip]]-ii)+1, jp, indinin[preorder[ip]]+1,ji))
        n = len(preorder)
        return buildtree(0,n-1,0,n-1)
