# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node=head
        rev=None
        while node:
            tmp=node.next
            node.next=rev
            rev=node
            node=tmp
        return rev


