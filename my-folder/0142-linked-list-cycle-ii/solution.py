# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodes_seen=set()
        node=head
        while node is not None:
            if node in nodes_seen:
                return node
            else:
                nodes_seen.add(node)
                node=node.next
        return None
