# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(root):
            if root == None:
                return 0
            left, right = dfs(root.left), dfs(root.right)
            s = root.val+left+right
            cnt[s] += 1
            return s
        cnt = Counter()
        dfs(root)
        mx = max(cnt.values())
        return [k for k,v in cnt.items() if v==mx]
        
