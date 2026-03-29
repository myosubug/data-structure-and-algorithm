# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodes = []
        cur = head

        while cur:
            nodes.append(cur)
            cur = cur.next

        # 4 - 2 = 2
        target = len(nodes) - n

        if target == 0:
            return head.next
        
        nodes[target-1].next = nodes[target].next

        return head