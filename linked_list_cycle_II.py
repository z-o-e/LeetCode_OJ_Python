# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a list node
    def detectCycle(self, head):
        
        if head==None:
            return None
            
        slow = fast = head
        
        while fast.next!=None and fast.next.next!=None:
            slow = slow.next
            fast = fast.next.next
            if slow==fast:
                break
            
        if fast.next==None or fast.next.next==None:
            return None
            
        fast = head
        while slow!=fast:
            slow = slow.next
            fast = fast.next
            
        return slow
        