# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        
        if head==None:
            return False
        
        # fast one take two steps at a time, slow one takes one
        # slow can catch up with the fast one, then it is cycled    
        fast = slow = head
        
        while fast.next!= None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                break
            
        if fast.next!=None and fast.next.next != None :
            return True
        return False
        