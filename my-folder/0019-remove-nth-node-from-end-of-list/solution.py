# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        f=head
        s=head
        
        for i in range(n+1):
            if not f:
                return head.next
            f=f.next
        while f:
            f=f.next
            s=s.next
        s.next=s.next.next
        return head
