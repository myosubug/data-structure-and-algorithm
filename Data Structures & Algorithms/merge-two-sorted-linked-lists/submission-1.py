# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        h1 = list1
        h2 = list2
        ret = ListNode()
        ret2 = ret
        while h1 and h2:
            if h1.val <= h2.val:
                ret.next = h1
                h1 = h1.next
            else:
                ret.next = h2
                h2 = h2.next
            ret = ret.next
        
        if h1:
            ret.next = h1
        elif h2:
            ret.next = h2

        return ret2.next