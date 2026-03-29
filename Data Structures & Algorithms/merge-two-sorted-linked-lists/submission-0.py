# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head1 = list1
        head2 = list2

        ret = ListNode()
        ret2 = ret

        while head1 and head2:
            if head1.val < head2.val:
                ret.next = head1
                head1 = head1.next
            else:
                ret.next = head2
                head2 = head2.next
            ret = ret.next
   

        if head1:
            ret.next = head1
        elif head2:
            ret.next = head2

        return ret2.next