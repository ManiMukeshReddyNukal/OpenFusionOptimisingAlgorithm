# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        resp=[[-1 for _ in range(n)] for _ in range(m)]
        moves=[[0,1],[1,0],[0,-1],[-1,0]]
        i,j=0,0
        cur_d=0
        while head:
            resp[i][j]=head.val
            newi,newj=i+moves[cur_d][0],j+moves[cur_d][1]
            if (min(newi, newj)<0 or newi>=m or newj>=n or resp[newi][newj]!=-1):
                cur_d=(cur_d+1)%4
            i+=moves[cur_d][0]
            j+=moves[cur_d][1]
            head=head.next
        return resp
