# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        cur=head
        dummy=ListNode(0,head)
        pre=dummy
        while cur and cur.next:
            if cur.val==cur.next.val:
                while cur and cur.next and cur.val==cur.next.val:
                    cur=cur.next
                pre.next=cur.next
            else:
                pre=pre.next
            cur=cur.next
        return dummy.next
                
