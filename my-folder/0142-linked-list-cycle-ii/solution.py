# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        visited=set()
        node=head
        while node:
            nxt=node.next
            if node in visited:
                return node 
            visited.add(node)
            node=nxt
        
        
