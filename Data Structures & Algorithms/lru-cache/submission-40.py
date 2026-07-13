class Node:
    def __init__(self, key=-1, val=-1):
        self.key = key
        self.val = val
        self.pre = None
        self.nex = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.lookup = {}
        self.head = Node()
        self.tail = Node()
        self.head.nex = self.tail
        self.tail.pre = self.head
        

    def get(self, key: int) -> int:
        if key in self.lookup:
            current = self.lookup[key]
            self.remove(current)
            self.insertToFront(current)
            return current.val
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        new_node = Node(key, value)
        if key in self.lookup:
            old_node = self.lookup[key]
            self.lookup[key] = new_node
            self.remove(old_node)
            self.insertToFront(new_node)
        else:
            self.lookup[key] = new_node
            self.insertToFront(new_node)
            if len(self.lookup) > self.cap:
                deleting = self.tail.pre
                self.remove(deleting)
                del self.lookup[deleting.key]
    
    def remove(self, node):
        pre = node.pre
        nex = node.nex

        pre.nex = nex
        nex.pre = pre

    def insertToFront(self, node):
        next_node = self.head.nex

        self.head.nex = node
        node.pre = self.head

        node.nex = next_node
        next_node.pre = node