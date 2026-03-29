class Node:
    def __init__(self, key=-1, value=-1):
        self.key = key
        self.val = value
        self.nex = None
        self.pre = None

class LRUCache:
    def __init__(self, capacity):
        self.cap = capacity
        self.start = Node()
        self.end = Node()
        self.lookup = {}

        self.start.nex = self.end
        self.end.pre = self.start
    
    def get(self, key):
        if key in self.lookup:
            node = self.lookup[key]
            self.delete_node(node)
            self.lookup[key] = node
            self.insert_front(node)
            return node.val
        else:
            return -1
    
    def put(self, key, value):
        if key in self.lookup:
            node = self.lookup[key]
            node.val = value
            self.delete_node(self.lookup[key])
            self.lookup[key] = node
            self.insert_front(node)
        else:
            new_node = Node(key, value)
            self.lookup[key] = new_node
            self.insert_front(new_node)
            if len(self.lookup) > self.cap:
                self.delete_node(self.end.pre)
    
    def insert_front(self, node):
        next_node = self.start.nex
        # self.start <-> node
        self.start.nex = node
        node.pre = self.start

        #node <-> next_node
        node.nex = next_node
        next_node.pre = node

    def delete_node(self, node):
        p, n = node.pre, node.nex
        # removing references from DLL
        p.nex = n
        n.pre = p

        # removing refernece from self.lookup
        if node.key in self.lookup:
            del self.lookup[node.key]




        
