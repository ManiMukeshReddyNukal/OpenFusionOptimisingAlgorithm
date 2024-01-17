class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head

        # Create a dummy node to simplify edge cases
        dummy = ListNode(0, head)
        prev = dummy

        # Move prev to the node just before the left position
        for _ in range(left - 1):
            prev = prev.next

        # Start the reversal process
        reverse = None
        cur = prev.next
        for _ in range(right - left + 1):
            nxt = cur.next
            cur.next = reverse
            reverse = cur
            cur = nxt

        # Connect the reversed sublist back to the main list
        prev.next.next = cur
        prev.next = reverse

        return dummy.next

