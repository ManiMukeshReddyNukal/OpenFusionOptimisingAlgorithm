# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        num=head.val
        base=1
        node=head
        while node.next:
            num=num*2+node.next.val
            node=node.next
        return num
