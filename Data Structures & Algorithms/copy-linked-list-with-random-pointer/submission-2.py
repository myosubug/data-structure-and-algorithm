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
        lookup = {None: None}
        dummy = head
        while dummy:
            copy = Node(dummy.val)
            lookup[dummy] = copy
            dummy = dummy.next

        dummy = head
        while dummy:
            copy = lookup[dummy]
            copy.next = lookup[dummy.next]
            copy.random = lookup[dummy.random]
            dummy = dummy.next

        return lookup[head]
        