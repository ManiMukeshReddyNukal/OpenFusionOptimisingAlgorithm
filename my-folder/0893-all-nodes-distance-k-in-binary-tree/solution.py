# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        q=deque([root])
        graph= defaultdict(list)
        while q:
            node = q.pop()
            if node.left:
                graph[node].append(node.left)
                graph[node.left].append(node)
                q.append(node.left)
            if node.right:
                graph[node].append(node.right)
                graph[node.right].append(node)
                q.append(node.right)
        distance=-1
        q=deque([target])
        visited=set()
        while q:
            distance+=1
            n=len(q)
            if distance==k:
                return [node.val for node in q]
            for i in range(n):
                node = q.pop()
                visited.add(node)
                for adjnode in graph[node]:
                    if adjnode in visited: continue
                    q.appendleft(adjnode)
        return []
