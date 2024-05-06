# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack=[]
        current=head
        while current:
            stack.append(current)
            current=current.next
        current=stack.pop()
        maximum_so_far=current.val
        result_list=ListNode(maximum_so_far)
        while stack:
            current=stack.pop()
            if current.val>=maximum_so_far:
                maximum_so_far=current.val
                new_node=ListNode(current.val)
                new_node.next=result_list
                result_list=new_node
            else:
                continue
        return result_list

