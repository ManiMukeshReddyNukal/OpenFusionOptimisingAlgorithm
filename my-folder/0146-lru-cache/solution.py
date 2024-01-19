class ListNode:
    def __init__(self,key,val):
        self.key=key
        self.val=val
        self.pre=None
        self.next=None
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.dic={}
        self.head=ListNode(-1,-1)
        self.tail=ListNode(-1,-1)
        self.head.next=self.tail
        self.tail.pre=self.head
    
    # to remove from in btwn the list 
    def remove(self,node):
        node.pre.next=node.next
        node.next.pre=node.pre
    
    # to add to the top of queue
    def add(self,node):
        previous_end=self.tail.pre
        previous_end.next=node
        node.pre=previous_end
        node.next=self.tail
        self.tail.pre=node
        

    def get(self, key: int) -> int:
        if key not in self.dic:
            return -1
        node=self.dic[key]
        self.remove(node)
        self.add(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            old_node=self.dic[key]
            self.remove(old_node)
        node=ListNode(key,value)
        self.dic[key]=node
        self.add(node)
        if len(self.dic)>self.capacity:
            node_to_delete=self.head.next
            self.remove(node_to_delete)
            del self.dic[node_to_delete.key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
