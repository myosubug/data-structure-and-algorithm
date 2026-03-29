# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        nodes = []
        ret = ListNode()

        for li in lists:
            cur = li
            while cur:
                nodes.append(cur)
                cur = cur.next


        nodes.sort(key = lambda n: n.val)

        for i in range(len(nodes)-1):
            nodes[i].next = nodes[i+1]

        if len(nodes) > 0:
            ret.next = nodes[0]

        return ret.next