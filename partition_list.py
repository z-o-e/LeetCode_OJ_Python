# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param x, an integer
    # @return a ListNode
    def partition(self, head, x):
        if not head:
            return head
        
        leftHead = left = ListNode(0)
        rightHead = right = ListNode(0)
        
        while head!=None:
            if head.val < x:
                left.next = head
                left = head
            else:
                right.next = head
                right = head
                
            head = head.next
            
        left.next = rightHead.next 
        right.next = None
        
        return leftHead.next
                