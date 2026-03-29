

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None

        nodes = []
        ret = ListNode()

        for li in lists:
            cur = li
            while cur:
                nodes.append(cur)
                cur = cur.next

        
        nodes.sort(key = lambda w: w.val)

        ret.next = nodes[0]
        for i in range(len(nodes)-1):
            nodes[i].next = nodes[i+1]

        return ret.next

