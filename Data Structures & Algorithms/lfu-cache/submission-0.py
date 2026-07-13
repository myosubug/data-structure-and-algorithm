class Node:
    def __init__(self, key=-1, val=-1):
        self.key = key
        self.val = val
        self.pre = None
        self.nex = None
        self.freq = 1

class DLL:

    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.nex = self.tail
        self.tail.pre = self.head
        
    def remove(self, node):
        pre = node.pre
        nex = node.nex

        pre.nex = nex
        nex.pre = pre
    
    def remove_last(self):
        last = self.tail.pre
        self.remove(last)
        return last

    def insertToFront(self, node):
        next_node = self.head.nex

        self.head.nex = node
        node.pre = self.head

        node.nex = next_node
        next_node.pre = node

    def is_empty(self):
        return self.head.nex == self.tail

class LFUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.lookup = {}
        self.freq_lookup = defaultdict(DLL)
        self.min_freq = 0

        
    def get(self, key: int) -> int:
        if key in self.lookup:
            current_node = self.lookup[key]
            current_freq = current_node.freq
            self.freq_lookup[current_freq].remove(current_node)
            if self.freq_lookup[current_freq].is_empty() and current_freq == self.min_freq:
                self.min_freq += 1
            current_node.freq += 1
            new_freq = current_node.freq
            self.freq_lookup[new_freq].insertToFront(current_node)
            return current_node.val
        else:
            return -1    

        
    def put(self, key: int, value: int) -> None:
        if key in self.lookup:
            current_node = self.lookup[key]
            current_node.val = value
            current_freq = current_node.freq
            self.freq_lookup[current_freq].remove(current_node)
            if self.freq_lookup[current_freq].is_empty() and current_freq == self.min_freq:
                self.min_freq += 1
            current_node.freq += 1
            new_freq = current_node.freq
            self.freq_lookup[new_freq].insertToFront(current_node)
        else:
            if len(self.lookup) >= self.cap:
                last = self.freq_lookup[self.min_freq].remove_last()
                del self.lookup[last.key]
            new_node = Node(key, value)        
            self.lookup[key] = new_node
            new_freq = new_node.freq
            self.freq_lookup[new_freq].insertToFront(new_node)
            self.min_freq = 1
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)