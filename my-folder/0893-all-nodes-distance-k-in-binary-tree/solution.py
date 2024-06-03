# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if k==0:
            return [target.val]
        graph=defaultdict(list)
        q=deque([root])
        while q:
            node=q.popleft()
            if node.left:
                graph[node].append(node.left)
                graph[node.left].append(node)
                q.append(node.left)
            if node.right:
                graph[node].append(node.right)
                graph[node.right].append(node)
                q.append(node.right)
        dist=-1
        visited=set()
        q=deque([target])
        while q :
            noofnodes=len(q)
            dist+=1
            if dist==k:
                return [ node.val for node in q]
            for i in range(noofnodes):
                node=q.popleft()
                visited.add(node)
                for adjnodes in graph[node]:
                    if adjnodes in visited: continue
                    q.append(adjnodes)
        return []
