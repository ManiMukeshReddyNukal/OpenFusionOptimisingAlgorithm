"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def __init__(self):
        self.visited={}
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return
        if node.val in self.visited:
            return self.visited[node.val]
        cp=Node(node.val)
        self.visited[node.val]=cp
        ns=node.neighbors
        cns=[]
        for nd in ns:
            cns.append(self.cloneGraph(nd))
        cp.neighbors=cns
        return cp
