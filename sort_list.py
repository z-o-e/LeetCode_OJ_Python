# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def sortList(self, head):
        if head==None or head.next==None:
            return head
        
        slow = head
        fast = head
        while fast.next.next and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        p, q = head, slow.next
        
        
        p = self.sortList(p)
        q = self.sortList(q)
        res = self.merge(p,q)
        
        return res
    
    def merge(self, p, q):
        if p==None:
            return q
        if q==None:
            return p
            
        
        dummy = ListNode(-1)
        pq = dummy
        
        while p and q:
            if p.val > q.val:
                pq.next = q
                q = q.next
            else:
                pq.next = p
                p = p.next
                
            pq = pq.next
            
        if p==None:
            pq.next = q
        if q==None:
            pq.next = p
            
        return dummy.next
