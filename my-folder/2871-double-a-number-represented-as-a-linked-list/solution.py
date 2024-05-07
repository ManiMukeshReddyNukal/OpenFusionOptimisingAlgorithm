# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current=head
        stack=[]
        while current:
            stack.append(current.val)
            current=current.next
        prev=None
        carry=0
        while stack:
            value = 2*stack.pop()
            node=TreeNode(value%10+carry)
            carry=value//10
            node.next=prev
            prev=node
        if carry>0:
            prev=node
            node=TreeNode(carry)
            node.next=prev
        return node
