# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        walker, runner = head, head

        while runner and runner.next:
            walker = walker.next
            runner = runner.next.next
            if walker == runner:
                return True

        return False