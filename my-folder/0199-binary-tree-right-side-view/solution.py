# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = []
        queue.append(root)
        right_view = []
        if root == None:
            return []
        while len(queue) != 0:
            back = queue[- 1]
            right_view.append(back.val)
            level_queue = []
            while queue != []:
                front = queue.pop(0)
                if front.left != None:
                    level_queue.append(front.left)
                if front.right != None:
                    level_queue.append(front.right)
            queue = level_queue
        # print(right_view)
        return right_view
