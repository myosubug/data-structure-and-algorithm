class ListNode:
    def __init__(self, key=-1, val=-1):
        self.key = key
        self.val = val
        self.nex = None
        self.pre = None


class LRUCache:

    def __init__(self, capacity: int):
        self.nodes = {}
        self.head = ListNode()
        self.tail = ListNode()
        self.head.nex = self.tail
        self.tail.pre = self.head
        self.cap = capacity

    def get(self, key: int) -> int:
        if key in self.nodes:
            val = self.nodes[key].val
            self.insert(key)
            return val
        else:
            return -1
        

    def put(self, key: int, value: int) -> None: 
        if key in self.nodes:
            self.nodes[key].val = value
        else:
            node = ListNode(key, value)
            self.nodes[key] = node
        self.insert(key)
        if len(self.nodes) > self.cap:
            self.remove()
        
    
    def remove(self):
        node = self.tail.pre
        key = node.key
        pre, nex = node.pre, self.tail
        pre.nex = nex
        nex.pre = pre
        del self.nodes[key]
    
    def insert(self, key):
        node = self.nodes[key]
        if node.pre and node.nex:
            node.pre.nex = node.nex
            node.nex.pre = node.pre
            
        head = self.head
        head_next = head.nex

        head.nex = node
        node.pre = head
        node.nex = head_next
        head_next.pre = node