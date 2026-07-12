class Node:
    def __init__(self, key=-1, val=-1):
        self.key = key
        self.val = val
        self.nex = None
        self.pre = None

class LRUCache:

    def __init__(self, capacity: int):
        self.lookup = {}
        self.head = Node()
        self.tail = Node()
        self.head.nex = self.tail
        self.tail.pre = self.head
        self.cap = capacity

    def get(self, key: int) -> int:
        if key in self.lookup:
            self.deleteInDll(self.lookup[key])
            self.insertToFront(self.lookup[key])
            return self.lookup[key].val
        else:
            return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.lookup:
            self.lookup[key].val = value
            self.deleteInDll(self.lookup[key])
            self.insertToFront(self.lookup[key])
        else:
            new_node = Node(key, value)
            self.lookup[key] = new_node
            self.insertToFront(new_node)
            if len(self.lookup) > self.cap:
                self.deleteAtLast()

    def insertToFront(self, node):
        current_front = self.head.nex

        self.head.nex = node
        node.pre = self.head

        node.nex = current_front
        current_front.pre = node
    
    def deleteAtLast(self):
        last_node = self.tail.pre
        second_last_node = last_node.pre

        second_last_node.nex = self.tail
        self.tail.pre = second_last_node

        del self.lookup[last_node.key]

    def deleteInDll(self, node):
        previous_node = node.pre
        next_node = node.nex

        previous_node.nex = next_node
        next_node.pre = previous_node