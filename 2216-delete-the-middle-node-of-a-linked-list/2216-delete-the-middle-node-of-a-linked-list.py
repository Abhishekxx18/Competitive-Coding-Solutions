# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return 
        dummy = ListNode()
        dummy.next = head
        slow = dummy
        fast = head

        while fast and fast.next :
            slow = slow.next
            fast = fast.next.next
        slow.next = slow.next.next 
        return head       
