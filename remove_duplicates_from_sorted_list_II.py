# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):

        if head==None:
            return head
        
        dummy = ListNode(-1)
        dummy.next = head
        pre = dummy
        cur = dummy.next
        
        while cur != None:
            dup = False
            
            while cur != None and cur.next != None and cur.val == cur.next.val:
                cur.next = cur.next.next
                dup = True
            
            if dup:
                pre.next = cur.next
                cur = pre.next
                continue
            
            pre = cur
            cur = cur.next
                
        return dummy.next 
        