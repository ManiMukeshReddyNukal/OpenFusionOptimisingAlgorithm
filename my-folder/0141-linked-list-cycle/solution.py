class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        sp, fp = head, head.next
        while fp and fp.next:
            sp = sp.next
            fp = fp.next.next
            if sp == fp:
                return True
        return False

