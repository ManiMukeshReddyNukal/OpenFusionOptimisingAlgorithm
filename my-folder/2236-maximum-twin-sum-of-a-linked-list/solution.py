# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow,fast=head,head
        maxsum=0
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        cur,rev=slow,None
        while cur:
            tmp=cur.next
            cur.next=rev
            rev=cur
            cur=tmp
        # return rev
        node=head
        while rev:
            maxsum=max(maxsum,node.val+rev.val)
            rev=rev.next
            node=node.next
        return maxsum
