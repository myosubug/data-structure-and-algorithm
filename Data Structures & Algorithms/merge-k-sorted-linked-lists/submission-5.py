# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class NodeWrapper:
    def __init__(self, node):
        self.node = node

    def __lt__(self, other):
        return self.node.val < other.node.val


class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None

        minheap = []
        dummy = ListNode()
        ret = dummy

        for l in lists:
            heapq.heappush(minheap, NodeWrapper(l))

        while minheap:
            popped = heapq.heappop(minheap)
            dummy.next = popped.node
            dummy = dummy.next
            if popped.node.next:
                heapq.heappush(minheap, NodeWrapper(popped.node.next))

        return ret.next


        