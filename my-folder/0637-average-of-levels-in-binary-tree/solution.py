# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        queue=[]
        res=[]
        queue.append(root)
        while queue:
            levlen=len(queue)
            temp=0
            for i in range(levlen):
                node=queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                temp+=node.val
            res.append(temp/levlen)
        return res
