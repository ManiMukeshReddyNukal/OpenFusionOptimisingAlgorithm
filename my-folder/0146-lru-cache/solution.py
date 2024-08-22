class TreeNode:
    def __init__(self,key,value):
        self.key=key
        self.value= value
        self.prev=None
        self.next=None
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity=capacity
        self.dic = {}
        self.head=TreeNode(-1, -1)
        self.tail=TreeNode(-1, -1)
        self.head.next=self.tail
        self.tail.prev=self.head


    # remove from middle of linkedlist 
    def remove(self, node:TreeNode):
        node.prev.next=node.next
        node.next.prev=node.prev
    
    # add at the 
    def add(self, node: TreeNode):
        temp = self.head.next
        node.next=temp
        temp.prev=node
        self.head.next=node
        node.prev=self.head

    def get(self, key: int) -> int:
        if key not in self.dic:
            return -1
        node = self.dic[key]
        # remove from position 
        # add at head
        self.remove(node)
        self.add(node)
        return node.value
        

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            old_node=self.dic[key]
            self.remove(old_node)
        node = TreeNode(key, value)
        self.dic[key]=node
        self.add(node)
        if (len(self.dic)>self.capacity):
            node_to_delete=self.tail.prev
            del self.dic[node_to_delete.key]
            self.remove(node_to_delete)



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
