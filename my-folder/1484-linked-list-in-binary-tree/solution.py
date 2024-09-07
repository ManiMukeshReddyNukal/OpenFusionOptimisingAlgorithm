# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        q=[root]
        while q:
            node=q.pop()
            if self.isMatch(node,head):
                return True
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return False
        
    def isMatch(self,node,head):
        if not node:
            return False
        stack=[(node,head)]
        while stack:
            curr_node,curr_lst=stack.pop()
            while curr_node and curr_lst:
                if curr_lst.val!=curr_node.val:
                    break
                curr_lst=curr_lst.next
                if curr_lst:
                    if curr_node.left:
                        stack.append((curr_node.left,curr_lst))
                    if curr_node.right:
                        stack.append((curr_node.right,curr_lst))
                break
            if not curr_lst:
                return True
        return False
