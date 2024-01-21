# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.order=self.createLinkedList(root)
    def createLinkedList(self, root: Optional[TreeNode]) -> ListNode:
        if root is None:
            return None
        left = self.createLinkedList(root.left)
        node=ListNode(root.val)
        right= self.createLinkedList(root.right)
        if left:
            last_left=left
            while last_left.next:
                last_left=last_left.next
            last_left.next=node
            node.next=right
            return left
        else:
            node.next=right
            return node

    def next(self) -> int:
        if not self.order:
            return None
        out=self.order
        self.order=self.order.next
        return out.val

    def hasNext(self) -> bool:
        return self.order is not None


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
