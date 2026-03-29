# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        walker = head
        if not head.next:
            return False
        jumper = head.next.next


        while walker and jumper:
            if walker == jumper:
                return True
            walker = walker.next
            jumper = jumper.next.next


        return False