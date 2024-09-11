from collections import defaultdict, deque
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        
        # Function to construct the tree into an undirected graph
        def constructTree(node, parent, graph):
            if not node:
                return
            # Add the bidirectional edge between parent and child
            if parent is not None:
                graph[node.val].add(parent)
                graph[parent].add(node.val)
            # Recursive calls to build for left and right children
            if node.left:
                constructTree(node.left, node.val, graph)
            if node.right:
                constructTree(node.right, node.val, graph)

        # Build the graph from the tree
        graph = defaultdict(set)
        constructTree(root, None, graph)
        
        # BFS to find the furthest distance from the start node
        q = deque([start])
        visited = set([start])
        distance = 0
        
        while q:
            n = len(q)
            for _ in range(n):
                current = q.popleft()
                # Explore neighbors (adjacent nodes in the graph)
                for neighbor in graph[current]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        q.append(neighbor)
            distance += 1
        
        return distance-1

