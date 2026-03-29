# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        store = []
        dummy = head
        while dummy:
            store.append(dummy)
            dummy = dummy.next

        nth_idx = len(store)-n
        if nth_idx == 0:
            return head.next

        prev, nth = store[nth_idx-1], store[nth_idx]
        prev.next = nth.next

        return head