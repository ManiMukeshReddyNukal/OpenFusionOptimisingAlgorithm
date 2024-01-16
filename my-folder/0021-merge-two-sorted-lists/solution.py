# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        h1=list1
        h2=list2
        prehead=ListNode(-1)
        prev=prehead
        while h1 and h2:
            if h1.val<h2.val:
                prev.next=h1
                h1=h1.next
            else:
                prev.next=h2
                h2=h2.next
            prev=prev.next
        prev.next=h1 if h1 is not None else h2
        return prehead.next
