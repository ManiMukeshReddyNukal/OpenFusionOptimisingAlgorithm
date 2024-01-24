# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        d=defaultdict(int)
        q=[]
        count=[0]
        q.append(root)
        def dfs(node,d):
            if not node:
                return None
            d[node.val]+=1
            if not node.left and not node.right:
                count[0]+=check(d)
            if node.left:
                dfs(node.left,d)
            if node.right:
                dfs(node.right,d)
            d[node.val]-=1
        def check(dic):
            cp=0
            for c in dic:
                if dic[c]%2==1:
                    cp+=1
            if cp>1:
                return 0
            else:
                return 1
        dfs(root,defaultdict(int))
        return count[0]
