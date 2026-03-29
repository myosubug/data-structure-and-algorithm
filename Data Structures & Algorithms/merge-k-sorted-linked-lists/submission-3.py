# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ret = []
        dummy = ListNode()
        ret_dummy = dummy
        for l in lists:
            while l:
                ret.append(l.val)
                l = l.next

        ret.sort()
        
        for n in ret:
            dummy.next =  ListNode(n)
            dummy = dummy.next

        return ret_dummy.next

        