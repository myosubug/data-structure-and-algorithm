class Node:
    def __init__(self, key=-999, val=-999):
        self.prev = None
        self.next = None
        self.key = key
        self.val = val

class LRUCache:
    def __init__(self, capacity: int):
        self.head = Node()
        self.tail = Node()
        self.cap = capacity
        self.lookup = {}
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.lookup:
            self.insert(key)
            return self.lookup[key].val
        else:
            return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.lookup:
            node = self.lookup[key]
            node.val = value
            self.insert(key)
        else:
            new_node = Node(key, value)
            self.lookup[key] = new_node
            self.insert(key)
            if len(self.lookup) > self.cap:
                self.delete(self.tail.prev)

    def delete(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

        del self.lookup[node.key]

    def insert(self, key):
        node = self.lookup[key]
        if node.prev and node.next:
            node.prev.next = node.next
            node.next.prev = node.prev
        first_node = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = first_node
        first_node.prev = node
