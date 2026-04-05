# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        one_jumper = head
        two_jumper = head

        while two_jumper and two_jumper.next:
            one_jumper = one_jumper.next
            two_jumper = two_jumper.next.next
        
        return one_jumper
            