# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        r1 = head
        r2 = head.next

        while r1 and r2:
            if r1.val == r2.val:
               return True
            if not r1.next:
                break
            if not r2.next or not r2.next.next:
                break
            r1 = r1.next
            r2 = r2.next.next
        

        return False