# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow=fast=head
        middle=None
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        middle=slow
        rev=None
        node=middle
        while node:
            nxt=node.next
            node.next=rev
            rev=node
            node=nxt
        # rev is our rev list 
        # middle is our middle element
        first=head
        while rev.next:
            tmp1,tmp2=first.next,rev.next
            first.next,rev.next=rev,tmp1
            first,rev=tmp1,tmp2
        

        
