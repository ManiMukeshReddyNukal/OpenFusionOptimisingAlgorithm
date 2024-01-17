"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        cur=head
        cp=None
        if head is None:
            return None
        while cur:
            cur.next=Node(cur.val,cur.next,cur.random)
            cur=cur.next.next
        cur=head
        while cur and cur.next:
            if cur.random is not None:
                cur.next.random=cur.random.next
            cur=cur.next.next
        cur=head.next
        while cur and cur.next:
            cur.next=cur.next.next
            cur=cur.next
        return head.next            
