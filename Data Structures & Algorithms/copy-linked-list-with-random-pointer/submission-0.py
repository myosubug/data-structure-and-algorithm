"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dummy = head
        oldToCopy = {None: None}
        while dummy:
            copy = Node(dummy.val)
            oldToCopy[dummy] = copy
            dummy = dummy.next

        dummy = head

        while dummy:
            copy = oldToCopy[dummy]
            copy.next = oldToCopy[dummy.next]
            copy.random = oldToCopy[dummy.random]
            dummy = dummy.next

        return oldToCopy[head]




