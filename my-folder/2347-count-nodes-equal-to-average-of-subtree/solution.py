# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.count=0
    def postorder(self,root):
        if root is None:
            return 0,0
        left=self.postorder(root.left)
        right=self.postorder(root.right)
        sum=left[0]+right[0]+root.val
        nodecount=left[1]+right[1]+1
        if nodecount != 0 and sum // nodecount == root.val:
            self.count+=1
        return sum,nodecount

    def averageOfSubtree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.postorder(root)
        return self.count
        
