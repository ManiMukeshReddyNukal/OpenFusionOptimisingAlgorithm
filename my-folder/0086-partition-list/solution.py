class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # Two dummy nodes for the start of two partitions
        less_head = ListNode(0)
        greater_head = ListNode(0)
        
        # Two pointers for the end of two partitions
        less = less_head
        greater = greater_head
        
        # Traverse the original list
        while head:
            if head.val < x:
                less.next = head
                less = less.next
            else:
                greater.next = head
                greater = greater.next
            head = head.next
        
        # Connect the two partitions
        less.next = greater_head.next
        greater.next = None  # Important to avoid cycle in linked list

        # Return the head of the modified list
        return less_head.next

