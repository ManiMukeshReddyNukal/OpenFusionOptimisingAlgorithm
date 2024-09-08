# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        l=0
        dummy=ListNode()
        dummy.next=head
        while dummy.next:
            l+=1
            dummy=dummy.next
        length_of_each_part=l//k
        rem=l%k
        resp=[]
        curr=head
        for _ in range(k):
            dummy=ListNode()
            tempnode=dummy
            for _ in range(length_of_each_part):
                dummy.next=curr
                dummy=dummy.next
                curr=curr.next
            if rem>0:
                dummy.next=curr
                dummy=dummy.next
                curr=curr.next
                rem-=1
            dummy.next=None
            resp.append(tempnode.next)
        return resp
