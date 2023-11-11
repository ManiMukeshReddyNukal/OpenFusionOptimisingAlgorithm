# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return root
        q=collections.deque()
        q.append(root)
        ans=[]
        while q:
            level=[]
            for i in range(len(q)):
                val=q.popleft()
                level.append(val.val)
                if val.left is not None:
                    q.append(val.left)
                if val.right is not None:
                    q.append(val.right)
            ans.append(level)
        return ans
