from collections import deque, defaultdict
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], start: int, end: int) -> str:
        def pathtoroot(root, val):
            if root==None: return []
            if root.val==val: return [root]
            right = pathtoroot(root.right, val)
            left = pathtoroot(root.left, val)
            path = left or right
            if path:
                path.append(root)
            return path
        spath = pathtoroot(root, start)
        epath = pathtoroot(root, end)
        spath.reverse()
        epath.reverse()

        ind = 0
        for i in range(min(len(spath),len(epath))):
            if spath[i]==epath[i]:
                ind=i
            else: break
        
        path = []
        for i in range(len(spath)-1,ind,-1):
            path.append('U')
        for i in range(ind, len(epath)-1):
            if epath[i+1]==epath[i].right:
                path.append('R')
            else:
                path.append('L')
        return "".join(path)
        
        
        
        
        
        # adj = defaultdict(lambda:[0, 0, 0])
        # def popadj(root, adj):
        #     if not root: return
        #     popadj(root.left,adj)
        #     popadj(root.right,adj)
        #     adj[root.val][0] = root.left.val if root.left else 0
        #     adj[root.val][1] = root.right.val if root.right else 0
        #     if root.left: adj[root.left.val][2] = root.val
        #     if root.right: adj[root.right.val][2] = root.val
        # adj[root.val][2] = 0
        # popadj(root,adj)
        

