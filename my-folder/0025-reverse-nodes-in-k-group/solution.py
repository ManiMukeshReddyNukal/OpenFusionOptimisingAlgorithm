# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getKth(self,cur,k):
        while k>0 and cur:
            cur=cur.next
            k-=1
        return cur
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummyNode=ListNode(0,head)
        groupPrev=dummyNode
        while True:
            kth=self.getKth(groupPrev,k)
            if not kth:
                break
            groupnext=kth.next
            prev,cur=kth.next,groupPrev.next
            while cur!=groupnext:
                nxt=cur.next
                cur.next=prev
                prev=cur
                cur=nxt
            tmp=groupPrev.next
            groupPrev.next=kth
            groupPrev=tmp
        return dummyNode.next


