# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        n=len(lists)
        dummy = ListNode(None)
        current = dummy
        pq=[]
        for i,node in enumerate(lists):
            if node:
                heapq.heappush(pq,(node.val,i,node))
        while pq:
            min_element,index,node=heapq.heappop(pq)
            current.next=node
            current=current.next
            if node.next:
                heapq.heappush(pq,(node.next.val,index,node.next))
        return dummy.next
            
