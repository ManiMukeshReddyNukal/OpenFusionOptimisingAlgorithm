# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        queue = []  # queue to store for explore next that in next stemp
        res = [] 
        queue.append(root)
    
        while (queue) :  # explore the tree untill queue is empty
            qlen = len(queue)
            temp = 0
            for i in range(qlen):
                curr = queue.pop(0)
                temp += curr.val
                
                if curr.left :  # If left node is not null
                    queue.append(curr.left)
                if curr.right:  # If right node is not null
                    queue.append(curr.right)
            res.append(temp/qlen)
        return res
            
