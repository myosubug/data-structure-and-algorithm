class Node:
    def __init__(self, key=-55, value=-55):
        self.prev = None
        self.next = None
        self.key = key
        self.val = value

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.lookup = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        

    def get(self, key: int) -> int:
        if key in self.lookup:
            self.insert(key)
            return self.lookup[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.lookup:
            new_node = Node(key, value)
            self.lookup[key] = new_node
            self.insert(key)
            if len(self.lookup) > self.cap:
                self.delete(self.tail.prev)
        else:
            node = self.lookup[key]
            node.val = value
            self.insert(key)   



    def insert(self, key):
        node = self.lookup[key]
        # remove from linked list first if already exists
        if key in self.lookup and node.prev and node.next:
            pre = node.prev
            nex = node.next
            pre.next = nex
            nex.prev = pre

        current_first = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = current_first
        current_first.prev = node

    
    def delete(self, node):
        node_before_deleting_node = node.prev
        node_before_deleting_node.next = self.tail
        self.tail.prev = node_before_deleting_node

        del self.lookup[node.key]
