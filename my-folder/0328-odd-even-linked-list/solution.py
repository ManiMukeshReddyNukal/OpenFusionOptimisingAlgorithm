# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node=head
        if not node or not node.next:
            return head
        odd=node
        even=node.next
        evenhead=even
        while even and even.next:
            odd.next=even.next
            odd=odd.next
            even.next=even.next.next
            even=even.next
        odd.next=evenhead
        return head
        
