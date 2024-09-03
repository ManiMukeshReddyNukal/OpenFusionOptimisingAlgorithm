class TreeNode:
    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.prev=None
        self.next=None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.head=TreeNode(-1, -1)
        self.tail=TreeNode(-1, -1)
        self.head.next=self.tail
        self.tail.prev=self.head
        self.dict={}
    
    def remove(self,node):
        node.next.prev=node.prev
        node.prev.next=node.next
    
    def add(self,node):
        temp=self.head.next
        node.next=temp
        temp.prev=node
        self.head.next=node
        node.prev=self.head

    def get(self, key: int) -> int:
        if key not in self.dict:
            return -1
        node=self.dict[key]
        self.remove(node)
        self.add(node)
        return node.value

        

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            node=self.dict[key]
            self.remove(node)
        node=TreeNode(key, value)
        self.dict[key]=node
        self.add(node)
        if (len(self.dict)>self.capacity):
            node_to_delete=self.tail.prev
            self.remove(node_to_delete)
            del self.dict[node_to_delete.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
