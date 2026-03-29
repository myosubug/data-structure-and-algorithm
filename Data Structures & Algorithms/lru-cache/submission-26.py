class Node:
    def __init__(self, key=-999, val=-999):
        self.key = key
        self.val = val
        self.pre = None
        self.nex = None


class LRUCache:
    def __init__(self, capacity: int):
        self.head = Node()
        self.tail = Node()
        self.head.nex = self.tail
        self.tail.pre = self.head
        self.lookup = {}
        self.cap = capacity

    def get(self, key: int) -> int:
        if key not in self.lookup:
            return -1
        else:
            self.insert(self.lookup[key])
            return self.lookup[key].val
        # if key not exists -> return -1
        # else -> return value of the key
        # and insert the key after head

    def put(self, key: int, value: int) -> None:
        if key in self.lookup:
            self.lookup[key].val = value
            self.insert(self.lookup[key])
        else:
            new_node = Node(key, value)
            self.lookup[key] = new_node
            self.insert(new_node)
            if len(self.lookup) > self.cap:
                self.delete(self.tail.pre)
        # if key exists -> update the value of the key
        #    then insert the key after head
        # if key doesn't exist -> add new key-val
        #    then create and insert the key after head  
        # if len(self.lookup) > self.cap:
        #    delete the last node (node before tail)
    def insert(self, node):
        # remove from the current position if it was in the list
        # get head and head.next
        # insert between
        if node.pre and node.nex:
            prev_node = node.pre
            next_node = node.nex
            prev_node.nex = next_node
            next_node.pre = prev_node
        next_node = self.head.nex
        self.head.nex = node
        node.pre = self.head
        node.nex = next_node
        next_node.pre = node


    def delete(self, node):
        # get node.pre and node.nex
        # insert between
        prev_node = node.pre
        next_node = node.nex
        prev_node.nex = next_node
        next_node.pre = prev_node
        del self.lookup[node.key]
