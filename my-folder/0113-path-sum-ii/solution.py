# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def dfs(node,results,currentpath,currentSum):
            if not node:
                return
            currentpath.append(node.val)
            currentSum+=node.val
            if not node.left and not node.right:
                if currentSum==targetSum:
                    results.append(list(currentpath))
            else:
                dfs(node.left,results,currentpath,currentSum)
                dfs(node.right,results,currentpath,currentSum)
            currentpath.pop()
            currentSum-=node.val

        results=[]
        currentpath=[]
        dfs(root, results, currentpath, 0)
        return results
