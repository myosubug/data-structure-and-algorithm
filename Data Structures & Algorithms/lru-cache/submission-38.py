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



'''
Functional Requirements for Thread Safety
Your current implementation has race conditions. Here are the key issues:

Non-atomic operations: get() does multiple steps (lookup, delete, insert). Between steps, another thread could modify the cache.
Check-then-act pattern: In put(), you check if key in self.lookup, then act. Another thread could modify self.lookup between the check and the action.
Capacity check is unsafe: You insert first, then check if len(self.lookup) > self.cap. Between insertion and deletion, another thread could read an invalid state.
Dictionary access race: Multiple threads accessing self.lookup simultaneously without synchronization.
What You'd Need to Update
1. Add Locking Mechanism
You'd add a lock that protects the entire cache state:

import threading

class LRUCache:
    def __init__(self, capacity):
        self.cap = capacity
        self.lock = threading.Lock()  # Add this
        # ... rest of init
2. Wrap Critical Sections
Every method that reads/modifies the cache needs the lock:

def get(self, key):
    with self.lock:  # Acquire lock
        if key in self.lookup:
            node = self.lookup[key]
            self.delete_node(node)
            self.insert_front(node)
            return node.val
        return -1
    # Lock released here
3. Make Eviction Atomic
In put(), ensure the entire operation (insert + evict if needed) happens without interruption:

def put(self, key, value):
    with self.lock:
        if key in self.lookup:
            node = self.lookup[key]
            node.val = value
            self.delete_node(node)
            self.insert_front(node)
        else:
            new_node = Node(key, value)
            self.lookup[key] = new_node
            self.insert_front(new_node)
            if len(self.lookup) > self.cap:
                lru_node = self.end.pre
                self.delete_node(lru_node)
                # Note: delete_node already removes from self.lookup
'''


        
