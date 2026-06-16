class ListNode:
    def __init__(self, val=-1):
        self.value = val
        self.pre = None
        self.nex = None

class MyLinkedList:

    def __init__(self):
        self.head = ListNode()
        self.tail = ListNode()
        self.head.nex = self.tail
        self.tail.pre = self.head
        self.size = 0
    
    def print(self):
        cur = self.head
        ret = []
        while cur:
            ret.append(cur.value)
            cur = cur.nex
        print(ret)


    def get(self, index: int) -> int:
        if not (0 <= index < self.size) :
            return -1

        ret = None
        if index < self.size // 2:
            ret = self.head
            for i in range(index+1):
                ret = ret.nex
        else:
            ret = self.tail
            for j in range(self.size-index):
                ret = ret.pre
        return ret.value


    def addAtHead(self, val: int) -> None:
        p = self.head
        n = p.nex
        new_node = ListNode(val)
        p.nex = new_node
        new_node.pre = p
        new_node.nex = n
        n.pre = new_node
        self.size += 1

    def addAtTail(self, val: int) -> None:
        p = self.tail.pre
        n = self.tail
        new_node = ListNode(val)
        p.nex = new_node
        new_node.pre = p
        new_node.nex = n
        n.pre = new_node
        self.size += 1


    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return

        cur = self.head
        for i in range(index+1):
            cur = cur.nex
        p = cur.pre
        n = cur
        new_node = ListNode(val)
        p.nex = new_node
        new_node.pre = p
        new_node.nex = n
        n.pre = new_node
        self.size += 1


    def deleteAtIndex(self, index: int) -> None:
        if self.get(index) == -1 or index >= self.size:
            return

        cur = self.head
        for i in range(index+1):
            cur = cur.nex
        p = cur.pre
        n = cur.nex
        p.nex = n
        n.pre = p
        self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)