# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # find Nth node from front
        node = []
        cur = head

        while cur:
            node.append(cur)
            cur = cur.next
        
        target = len(node) - n

        if target == 0:
            return head.next
        
        node[target-1].next = node[target].next

        return head


        # remove