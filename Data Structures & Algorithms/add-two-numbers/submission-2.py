# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        remainder = 0
        dummy = ListNode()
        ret_dummy = dummy

        while carry or l1 or l2:
            l1val = l1.val if l1 else 0 
            l2val = l2.val if l2 else 0
            carry, remainder = divmod(l1val+l2val+carry, 10)
            
            dummy.next = ListNode(remainder, None)
            dummy = dummy.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return ret_dummy.next

