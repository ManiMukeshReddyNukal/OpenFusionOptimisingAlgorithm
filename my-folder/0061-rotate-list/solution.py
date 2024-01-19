# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k==0:
            return head
        last_node = head
        length = 1
        while last_node.next:
            last_node = last_node.next
            length += 1
        k %= length
        if k == 0:
            return head
        k=length-k
        cur=head
        for _ in range(k-1):
            cur=cur.next
        new_head=cur.next
        cur.next=None
        last_node.next=head
        return new_head
