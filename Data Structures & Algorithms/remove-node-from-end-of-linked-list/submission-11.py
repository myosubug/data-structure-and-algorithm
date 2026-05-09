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
        
        target_index = len(store) - n
        if target_index == 0:
            return head.next

        prev = store[target_index-1]
        n = store[target_index]

        prev.next = n.next

        return head