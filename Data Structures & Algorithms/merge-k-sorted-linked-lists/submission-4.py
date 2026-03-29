# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class NodeWrapper():
    def __init__(self, node):
        self.node = node
    def __lt__(self, other):
        return self.node.val < other.node.val


class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # BRUTE FORCE
        # ret = []
        # dummy = ListNode()
        # ret_dummy = dummy
        # for l in lists:
        #     while l:
        #         ret.append(l.val)
        #         l = l.next

        # ret.sort()
        
        # for n in ret:
        #     dummy.next =  ListNode(n)
        #     dummy = dummy.next

        # return ret_dummy.next
        dummy = ListNode()
        ret = dummy

        if len(lists) == 0:
            return None

        minheap = []
        for li in lists:
            if li:
                heapq.heappush(minheap, NodeWrapper(li))
        

        while minheap:
            wrapped_node = heapq.heappop(minheap)
            dummy.next = wrapped_node.node
            dummy = dummy.next
            if wrapped_node.node.next:
                heapq.heappush(minheap, NodeWrapper(wrapped_node.node.next))
        
        return ret.next



        