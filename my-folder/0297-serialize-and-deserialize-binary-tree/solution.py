# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        return ",".join(self.preorderTraversal(root))

    
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return ["None"]
        out=[]
        out.append(str(root.val))
        out.extend(self.preorderTraversal(root.left))
        out.extend(self.preorderTraversal(root.right))
        return out

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data_list=data.split(",")
        return self.constructBinary(data_list)

        
    def constructBinary(self,data_list):
        if data_list[0]=="None":
            data_list.pop(0)
            return None
        root=TreeNode(int(data_list.pop(0)))
        root.left=self.constructBinary(data_list)
        root.right=self.constructBinary(data_list)
        return root


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
