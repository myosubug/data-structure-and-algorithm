# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        
        dummy = ListNode(0, head)
        left_before_reverse = dummy
        cur = head

        for _ in range(left-1):
            left_before_reverse = cur
            cur = cur.next


        prev = None
        for _ in range(right-left+1):
            nex = cur.next
            cur.next = prev
            prev = cur
            cur = nex

        left_before_reverse.next.next = cur
        left_before_reverse.next = prev

        return dummy.next