# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return root
        ans=[]
        q=collections.deque()
        q.append(root)
        while q:
            ans.append(q[-1].val)
            for i in range(len(q)):
                val=q.popleft()
                if val.left is not None:
                    q.append(val.left)
                if val.right is not None:
                    q.append(val.right)
        return ans
