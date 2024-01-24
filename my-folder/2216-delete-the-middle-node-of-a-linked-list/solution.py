# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        s=head
        f=head.next
        if not f:
            return None
        while f and  f.next and f.next.next:
            s=s.next
            f=f.next.next
        s.next=s.next.next
        return head
