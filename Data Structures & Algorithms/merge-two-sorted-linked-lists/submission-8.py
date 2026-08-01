# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None

        dummy = ListNode()
        ret = dummy

        while list1 and list2:
            l1val = list1.val
            l2val = list2.val

            if l1val <= l2val:
                dummy.next = list1
                list1 = list1.next
            else:
                dummy.next = list2
                list2 = list2.next
            
            dummy = dummy.next
        
        if list1 and not list2:
            dummy.next = list1
        elif list2 and not list1:
            dummy.next = list2

        return ret.next
