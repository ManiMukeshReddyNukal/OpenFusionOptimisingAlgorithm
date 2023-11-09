# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def nodepath(self, root,p):
        if root.val == p:
            return [root.val]
        val = []
        if root.left != None:
            temp = self.nodepath(root.left, p)
            if(len(temp)!=0):
                val = [root.val]+(temp)
        
        if root.right != None:
            temp = self.nodepath(root.right, p)
            if(len(temp)!=0):
                val = [root.val]+(temp)
        
        return val
    
    def findDistance(self, root, p, q):
        """
        :type root: TreeNode
        :type p: int
        :type q: int
        :rtype: int
        """
        p1 = (self.nodepath(root, p))
        p2 = (self.nodepath(root, q))

        return len(set(p1)^set(p2))
    
    
