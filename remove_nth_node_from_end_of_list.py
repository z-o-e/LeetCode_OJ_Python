# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @return a ListNode
    def removeNthFromEnd(self, head, n):
        
        dummy = ListNode(-1)
        dummy.next = head
        # pointer first is n-step ahead of second
        first = second = dummy
        
        for i in range(n):
            first = first.next
            
        while first.next!=None:
            first = first.next
            second = second.next
        
        second.next = second.next.next
        
        return dummy.next