# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=head
        while dummy and dummy.next:
            node1=dummy
            node2=dummy.next
            node=ListNode(math.gcd(node1.val,node2.val))
            node.next=dummy.next
            dummy.next=node
            dummy=dummy.next.next
        return head

