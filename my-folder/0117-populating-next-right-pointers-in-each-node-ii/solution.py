"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        m={}
        def check( h:int,root:'Node')->'Node':
            if not root:
                return None
            if h not in m:
                m[h]=[]
            m[h].append(root)
            check(h+1,root.left)
            check(h+1,root.right)
        check(0,root)
        for key in m:
            nodes=m[key]
            for i in range(len(nodes)):
                if i==len(nodes)-1:
                    nodes[i].next=None
                else:
                    nodes[i].next=nodes[i+1]
        return root

    
    
        
