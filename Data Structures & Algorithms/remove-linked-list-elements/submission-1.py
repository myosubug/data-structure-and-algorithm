# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        new_head = ListNode()
        ret = new_head
        current = head


        while current:
            if current.val != val:
                new_head.next = current
                new_head = new_head.next

            current = current.next

        new_head.next = None
        return ret.next